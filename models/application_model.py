from schematics.models import Model
from schematics.types import StringType, URLType
from schematics.types.compound import ListType, ModelType


class Dependencies(Model):
    name = StringType(required=True)
    version = StringType(required=True)


class ApplicationModel(Model):
    name = StringType(required=True)
    website = URLType()
    dependencies = ListType(ModelType(Dependencies))


