from qgis.PyQt.QtCore import QCoreApplication

try:
    from asistente_ladm_col.config.keys.common import *
    from asistente_ladm_col.lib.model_registry import LADMColModel
except ModuleNotFoundError:
    pass

from ladm_col_add_on_ric.config.general_config import (RIC_MODEL_KEY,
                                                       MODELS_DIR)


class ModelConfig:

    def __init__(self):
        pass

    @staticmethod
    def get_model_instance():
        model_config = {
            MODEL_ALIAS: QCoreApplication.translate("ModelConfig", "RIC LADM-COL Model"),
            MODEL_IS_SUPPORTED: True,
            MODEL_SUPPORTED_VERSION: "0.1",
            MODEL_HIDDEN_BY_DEFAULT: False,
            MODEL_CHECKED_BY_DEFAULT: True,
            MODEL_MAPPING: dict(),
            MODEL_DIR: MODELS_DIR
        }
        return LADMColModel(RIC_MODEL_KEY, model_config)
