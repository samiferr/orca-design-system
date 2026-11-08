"""Class-based view mixin that fills the context ORCA's generic templates read.

    from orca.mixins import OrcaPageMixin

    class CameraList(OrcaPageMixin, ListView):
        model = Camera
        paginate_by = 25
        template_name = "orca/generic/list.html"
        list_columns = ["name", "site", "status", ("Counted today", "today")]
        detail_url_name, create_url_name = "camera-detail", "camera-create"
        update_url_name, delete_url_name = "camera-update", "camera-delete"

The same mixin works with DetailView (``detail_fields``), CreateView/UpdateView and DeleteView (which also gets
``blocked_by``: the protected or restricted objects that stop the delete, so the template can explain them).
"""

from __future__ import annotations

from django.db import models
from django.urls import NoReverseMatch, reverse

NUMERIC = (models.IntegerField, models.FloatField, models.DecimalField, models.DurationField)


def _columns(model, spec) -> list[dict]:
    out = []
    for item in spec:
        label, name = item if isinstance(item, (tuple, list)) else (None, item)
        numeric = False
        if model is not None:
            try:
                f = model._meta.get_field(name)
                label = label or str(f.verbose_name)
                numeric = isinstance(f, NUMERIC) and not f.choices
            except Exception:  # a property or method: label from the name
                pass
        label = str(label or name.replace("_", " "))
        out.append({"label": label[:1].upper() + label[1:], "name": name, "numeric": numeric})
    return out


def _url(name: str, obj=None) -> str:
    if not name:
        return ""
    try:
        return reverse(name, args=[obj.pk]) if obj is not None else reverse(name)
    except NoReverseMatch:
        return ""


class OrcaPageMixin:
    """Adds ``title``, ``subtitle``, ``model_name(_plural)``, ``columns``, ``fields``, breadcrumbs and URLs."""

    title = ""
    subtitle = ""
    list_columns: list = []
    detail_fields: list = []
    list_url_name = detail_url_name = create_url_name = update_url_name = delete_url_name = ""
    nav: list = []

    def get_orca_model(self):
        model = getattr(self, "model", None)
        obj = getattr(self, "object", None)
        if model is None and obj is not None:
            model = type(obj)
        if model is None and getattr(self, "queryset", None) is not None:
            model = self.queryset.model
        return model

    def get_title(self, obj=None) -> str:
        return self.title

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        model = self.get_orca_model()
        obj = getattr(self, "object", None)
        meta = model._meta if model is not None else None
        ctx.setdefault("model_name", str(meta.verbose_name) if meta else "")
        ctx.setdefault("model_name_plural", str(meta.verbose_name_plural) if meta else "")
        ctx.setdefault("title", self.get_title(obj))
        ctx.setdefault("subtitle", self.subtitle)
        ctx.setdefault("nav", self.nav)
        ctx.setdefault("columns", _columns(model, self.list_columns))
        ctx.setdefault("fields", _columns(model, self.detail_fields))
        for key in ("list", "create"):
            ctx.setdefault(f"{key}_url", _url(getattr(self, f"{key}_url_name")))
        for key in ("detail", "update", "delete"):
            ctx.setdefault(f"{key}_url_name", getattr(self, f"{key}_url_name"))
            if obj is not None:
                ctx.setdefault(f"{key}_url", _url(getattr(self, f"{key}_url_name"), obj))
        ctx.setdefault("cancel_url", ctx.get("detail_url") or ctx.get("list_url") or "")
        if "breadcrumbs" not in ctx and obj is not None and ctx.get("list_url"):
            ctx["breadcrumbs"] = [(ctx["model_name_plural"].capitalize(), ctx["list_url"]), (str(obj), "")]
        if obj is not None and hasattr(self, "delete") and "blocked_by" not in ctx and self.template_name_suffix == "_confirm_delete":
            ctx["blocked_by"] = blocked_by(obj)
        return ctx


def blocked_by(obj) -> list[str]:
    """Objects that stop ``obj`` from being deleted (protected or restricted foreign keys), as text."""
    from django.db import router
    from django.db.models.deletion import Collector, ProtectedError, RestrictedError

    collector = Collector(using=router.db_for_write(type(obj)))
    try:
        collector.collect([obj])
    except (ProtectedError, RestrictedError) as exc:
        found = getattr(exc, "protected_objects", None) or getattr(exc, "restricted_objects", None) or []
        return [str(o) for o in list(found)[:10]]
    return []
