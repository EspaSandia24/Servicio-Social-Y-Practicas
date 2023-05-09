from django.core.validators import FileExtensionValidator

documentos_validador = FileExtensionValidator(
    allowed_extensions=['pdf'],
    message="Sólo se permiten documentos PDF"
)