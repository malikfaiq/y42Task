from .strategies import LocalDriveUploadStrategy, CloudFileUploadStrategy

STORAGE_TYP_STRATEGIES = {
    "local": LocalDriveUploadStrategy,
    "cloud": CloudFileUploadStrategy,
}

FILE_FORMATS = ["json", "xml", "pdf", "bytes"]

STORAGE_DESTINATIONS = ["local_drive", "ftp", "cloud_storage"]
