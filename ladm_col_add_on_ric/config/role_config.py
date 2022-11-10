from qgis.PyQt.QtCore import QCoreApplication

try:
    from asistente_ladm_col.config.keys.common import *
    from asistente_ladm_col.config.gui.gui_config import GUI_Config
except ModuleNotFoundError:
    pass

from ladm_col_add_on_ric.config.general_config import *


class RoleConfig:

    def __init__(self):
        pass

    @staticmethod
    def get_role_configuration():
        gui_config = GUI_Config().get_gui_dict()
        gui_config[MAIN_MENU][0][WIDGET_NAME] = "RI&C LADM-COL"

        default_gui_config = GUI_Config().get_gui_dict(DEFAULT_GUI)
        default_gui_config[MAIN_MENU][0][WIDGET_NAME] = "RI&C LADM-COL"

        return RIC_ROLE_KEY, {
            ROLE_NAME: QCoreApplication.translate("RoleConfig", "RIC user"),
            ROLE_DESCRIPTION: QCoreApplication.translate("RoleConfig",
                                                         "The RIC user is in charge of structuring data for Cadastral Information Report."),
            ROLE_MODELS: {ROLE_SUPPORTED_MODELS: [LADMNames.LADM_COL_MODEL_KEY,
                                                  LADMNames.ISO19107_MODEL_KEY,
                                                  RIC_MODEL_KEY],
                          ROLE_HIDDEN_MODELS: [LADMNames.LADM_COL_MODEL_KEY,
                                               LADMNames.ISO19107_MODEL_KEY],
                          ROLE_CHECKED_MODELS: [RIC_MODEL_KEY]},
            ROLE_ACTIONS: [
                ACTION_ST_LOGIN,
                ACTION_ST_LOGOUT,
                ACTION_CHECK_QUALITY_RULES],
            ROLE_QUALITY_RULES: [],
            ROLE_GUI_CONFIG: {TEMPLATE_GUI: gui_config, DEFAULT_GUI: default_gui_config}
        }
