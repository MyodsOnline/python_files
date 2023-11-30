power_plants = {'Кольская АЭС': [],
                'Петрозаводская ТЭЦ': [],
                'Киришская ГРЭС': [],
                'Правобережная ТЭЦ (ТЭЦ-5)': [],
                'Северная ТЭЦ (ТЭЦ-21)': [],
                'Северо-Западная ТЭЦ': [],
                'Ленинградская АЭС': [],
                'Первомайская ТЭЦ (ТЭЦ-14)': [],
                'Юго-Западная ТЭЦ': [],
                'Южная ТЭЦ (ТЭЦ-22)': [],
                'Новгородская ТЭЦ': [],
                'Псковская ГРЭС': [],
                'Талаховская ТЭЦ': [],
                'Маяковская ТЭЦ': [],
                'Калининградская ТЭЦ-2': [],
                'Прегольская ТЭС': [],
                'Приморская ТЭС': [],
                'Печорская ГРЭС': []}

gen_app_complex = ['ЭНРГ.Б', 'ЭНРГ.ТГ', 'ЭНРГ.ОО']
grid_app_complex = ['ЛЭП.ЛЭП 110 кВ', 'ЛЭП.ЛЭП 750 кВ', 'ЛЭП.ЛЭП 400 кВ', 'ЛЭП.ЛЭП 330 кВ', 'ЛЭП.ЛЭП 220 кВ']

FIELDS = {
    'self_number': '№ свой',
    'alien_number': '№ чужой',
    'zvk_giver': 'Предприятие',
    'complex': 'Комплекс',
    'empty_field': '',
    'zvk_status': 'Состояние заявки',
    'subject': 'Объект',
    'equipment': 'Оборудование',
    'equipment_detail': 'Оборудование, выводимое в ремонт',
    'mode': 'Состояние оборудования по заявке',
    'program': 'Программа переключений',
    'use_in_mode': 'Актуализация',
    'start_date': 'Разрешенное время - начало',
    'end_date': 'Разрешенное время -  конец',
    'asked_start_date': 'Просимое время - начало',
    'repair_type': 'Ремонт',
    'zvk_type': 'Категория',
    'over_date': 'Просрочена',
    'ag': 'А\Г',
    'grounding': 'Заземление',
    'conditions': 'Условия производства',
}

complex = ['СДТУ.СДТУ Н', 'ЭНРГ.ГГ', 'ЭЛТ.Прочее ЭЛТ', 'ЭЛТ.СШ.СШ 330 кВ', 'РЗА.РЗ', 'ЭЛТ.АТ,Т.АТ,Т 750 кВ',
           'ЭЛТ.В.В 750 кВ', 'РЗА.ПА', 'ЭЛТ.АТ,Т.АТ,Т 330 кВ', 'ЭЛТ.В.В 330 кВ', 'ЭЛТ.СКРМ', 'ЭЛТ.ТН.ТН 330 кВ',
           'ЛЭП.ЛЭП 110 кВ', 'РЗА.РА.НПРЧ', 'ЭЛТ.СШ.СШ 400 кВ', 'ЭЛТ.СКРМ.БК.БК 330 кВ', 'РЗА.ПА.УПАСК', 'РЗА.РАСП',
           'ЛЭП.ЛЭП 750 кВ', 'ЭЛТ.Прочее ЭЛТ.УВ', 'ЭЛТ.СШ.СШ 220 кВ', 'ЭЛТ.Р.РШ.РШ 10 кВ', 'АСДУ.СС',
           'ЭЛТ.СКРМ.БК.БК 35 кВ', 'ЭЛТ.Р.РШ.РШ 330 кВ', 'РЗА.РА.АВРЧМ', 'ЭЛТ.АТ,Т.АТ,Т 400 кВ', 'ЭЛТ.ВУ.ВУ 400 кВ',
           'ЭНРГ.ТГ', 'РЗА', 'СДТУ.СДТУ ДЦ', 'ЭЛТ.В.В 400 кВ', 'ЭЛТ.В.В 110 кВ', 'ЭНРГ.Б', 'ЛЭП.ЛЭП 400 кВ',
           'ЛЭП.ЛЭП 330 кВ', 'ЛЭП.ЛЭП 220 кВ', 'ЭЛТ.В.В 220 кВ', 'АСДУ.ПАК', 'ЭНРГ.ОО', 'ЭЛТ.СКРМ.СК.СК 15,75 кВ',
           'ЭЛТ.СКРМ.СК.СК 10 кВ', 'ЭЛТ.СКРМ.БК.БК 400 кВ', 'РЗА.РА']

dc_ru = ['МЭС Северо-Запада', 'ОДУ Центра', 'Новгородское РДУ', 'Кольское РДУ', 'Ленинградское РДУ', 'Карельское РДУ',
         'Коми РДУ', 'Балтийское РДУ', 'Архангельское РДУ']

dc_eu = ['Litgrid AB', 'Elering AS', 'Litgrid AB', 'Augstsprieguma tikls']

my_folder = 'K:/disp_sl/ЛИЧНЫЕ ПАПКИ ОДС/Кузнецов/'
