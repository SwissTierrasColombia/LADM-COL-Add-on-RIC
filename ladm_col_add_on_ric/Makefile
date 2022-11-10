all: resources_rc.py i18n/LADM-COL-Add-on-RIC_es.qm

update_translations: i18n/LADM-COL-Add-on-RIC_locale.ts

clean:
	rm -f resources_rc.py
	rm -f i18n/LADM-COL-Add-on-RIC_es.qm
	rm -f *.pyc *~

resources_rc.py: resources.qrc
	pyrcc5 -o resources_rc.py resources.qrc

i18n/LADM-COL-Add-on-RIC_es.qm: i18n/LADM-COL-Add-on-RIC_es.ts
	lrelease i18n/LADM-COL-Add-on-RIC.pro

i18n/LADM-COL-Add-on-RIC_locale.ts: i18n/LADM-COL-Add-on-RIC.pro
	lupdate i18n/LADM-COL-Add-on-RIC.pro
