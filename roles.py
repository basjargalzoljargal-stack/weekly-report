
DEPARTMENTS = {
    'dotood_khyanalт': 'Дотоод хяналтын хэлтэс',
    'tsakhim_burtgel': 'Цахим бүртгэл, дүн шинжилгээний хэлтэс',
    'tolovlolt': 'Төлөвлөлт, дотоод ажлын хэлтэс',
}

ROLE_LABELS = {
    'head':           'Хэлтсийн дарга (хяналт)',
    'zorchil':        'Зөрчил хариуцсан',
    'neg_tseg':       '1 цэгийн үйлчилгээ',
    'bus_orgodol':    'Бүс хариуцсан (өргөдөл/гомдол)',
    'negtle_bus':     'Бүсийн нэгтгэгч',
    'tsakhim':        'Цахим бүртгэл',
    'hil':            'Хилийн хориг',
    'medee_too':      'Мэдээ, дүн шинжилгээ',
    'nekhemjlel':     'Шүүхийн нэхэмжлэл',
    'lavlagaa':       'Өр төлбөргүй лавлагаа',
    'lavlagaa_negtle':'Лавлагаа + нэгтгэгч',
    'orgodol_central':'Өргөдөл, гомдол (төв)',
    'dotood_ajil':    'Дотоод ажил, хүний нөөц',
    'surgalt':        'Сургалт',
    'negtle_main':    'Нэгтгэгч (ерөнхий)',
}

# Pre-loaded users
INITIAL_USERS = [
    # Дотоод хяналтын хэлтэс
    ('Х.Оюунболд', 'х/а',  'dotood_khyanalт', 'head'),
    ('Н.Нямжаргал', 'д/х', 'dotood_khyanalт', 'zorchil'),
    ('Д.Баасансүрэн', 'д/х','dotood_khyanalт', 'neg_tseg'),
    ('Э.Цэнгүүнзул', 'д/х', 'dotood_khyanalт', 'neg_tseg'),
    ('М.Нарантунгалаг', 'х/ч','dotood_khyanalт','neg_tseg'),
    ('А.Зая', 'д/х',        'dotood_khyanalт', 'bus_orgodol'),
    ('Б.Даваадорж', 'д/х',  'dotood_khyanalт', 'bus_orgodol'),
    ('М.Үүлэнсолонго', 'д/х','dotood_khyanalт','bus_orgodol'),
    ('Э.Батхишиг', 'х/ч',   'dotood_khyanalт', 'bus_orgodol'),
    ('М.Золбоо', 'х/ч',     'dotood_khyanalт', 'bus_orgodol'),
    ('М.Эрдэнэбаяр', 'х/ч', 'dotood_khyanalт', 'bus_orgodol'),
    ('Г.Алтансувд', 'х/ч',  'dotood_khyanalт', 'negtle_bus'),
    # Цахим бүртгэл, дүн шинжилгээний хэлтэс
    ('Г.Азжаргал', 'х/ч',   'tsakhim_burtgel', 'head'),
    ('Г.Жигжид', 'д/х',     'tsakhim_burtgel', 'tsakhim'),
    ('Д.Гантулга', 'д/х',   'tsakhim_burtgel', 'tsakhim'),
    ('Б.Золзаяа', 'д/х',    'tsakhim_burtgel', 'hil'),
    ('Э.Ганчимэг', 'а/х',   'tsakhim_burtgel', 'medee_too'),
    ('Ц.Үдвал', 'х/ч',      'tsakhim_burtgel', 'nekhemjlel'),
    ('З.Номин-Эрдэнэ', 'а/д','tsakhim_burtgel','lavlagaa_negtle'),
    # Төлөвлөлт, дотоод ажлын хэлтэс
    ('Э.Алтанцэцэг', 'д/х', 'tolovlolt',       'head'),
    ('Θ.Саруултуяа', 'д/х', 'tolovlolt',       'surgalt'),
    ('Д.Намуун', 'х/ч',     'tolovlolt',       'dotood_ajil'),
    ('М.Март', 'х/ч',       'tolovlolt',       'dotood_ajil'),
    ('Б.Золжаргал', 'а/х',  'tolovlolt',       'negtle_main'),
    ('Ч.Элбэг', 'д/х',      'tolovlolt',       'orgodol_central'),
]

# ─── FORM DEFINITIONS ─────────────────────────────────────────────────────────
# Each form = list of sections; each section = title + list of fields
# field types: 'number', 'text', 'textarea', 'percent'

ROLE_FORMS = {

    # ── 1 цэгийн үйлчилгээ ──────────────────────────────────────────────────
    'neg_tseg': [
        {
            'title': '1 цэгийн үйлчилгээ',
            'fields': [
                {'id': 'niit_irsen',         'label': 'Нийт хандсан иргэн',                           'type': 'number', 'unit': 'иргэн'},
                {'id': 'shdg_guitsetgel',     'label': 'Шийдвэр гүйцэтгэлийн талаар мэдээлэл авсан', 'type': 'number', 'unit': 'иргэн'},
                {'id': 'busad_asуudlaar',     'label': 'Бусад асуудлаар мэдээлэл авсан',              'type': 'number', 'unit': 'иргэн'},
                {'id': 'holbon_shiydsersen',  'label': 'Холбон шийдвэрлэсэн',                         'type': 'number', 'unit': 'иргэн'},
                {'id': 'lavlagaa_olgosон',    'label': 'Өр төлбөргүй лавлагаа олгосон',               'type': 'number', 'unit': 'иргэн/хуулийн этгээд'},
            ]
        }
    ],

    # ── Зөрчил ───────────────────────────────────────────────────────────────
    'zorchil': [
        {
            'title': 'Тухайн 7 хоногт',
            'fields': [
                {'id': 'gomDol_too',        'label': 'Хүлээн авсан зөрчлийн гомдол мэдээлэл',        'type': 'number', 'unit': 'ш'},
                {'id': 'torguul_hun',       'label': 'Торгуульд татагдсан',                           'type': 'number', 'unit': 'хүн'},
                {'id': 'torguul_dun',       'label': 'Торгуулийн мөнгөн дүн',                         'type': 'number', 'unit': '₮', 'step': 'any'},
                {'id': 'barivch_hun',       'label': 'Баривчлах шийтгэлд татагдсан',                  'type': 'number', 'unit': 'хүн'},
                {'id': 'albadan_surgalt',   'label': 'Албадан сургалтад хамрагдсан',                  'type': 'number', 'unit': 'хүн'},
            ]
        },
        {
            'title': 'Өссөн дүнгээр',
            'fields': [
                {'id': 'oss_niit',          'label': 'Нийт холбогдогч',                               'type': 'number', 'unit': 'хүн'},
                {'id': 'oss_hyalbar_hun',   'label': 'Хялбаршуулсан журмаар торгосон',                'type': 'number', 'unit': 'хүн'},
                {'id': 'oss_hyalbar_dun',   'label': 'Хялбаршуулсан журмаар торгосон дүн',            'type': 'number', 'unit': '₮', 'step': 'any'},
                {'id': 'oss_shalgan_hun',   'label': 'Зөрчил шалган шийдвэрлэх ажиллагаагаар торгосон','type': 'number', 'unit': 'хүн'},
                {'id': 'oss_shalgan_dun',   'label': 'Зөрчил шалган шийдвэрлэх ажиллагаагаар торгосон дүн','type': 'number', 'unit': '₮', 'step': 'any'},
                {'id': 'oss_huukhed_torguul_hun', 'label': 'Хүүхдийн тэтгэлэгтэй холбоотой торгосон', 'type': 'number', 'unit': 'хүн'},
                {'id': 'oss_huukhed_torguul_dun', 'label': 'Хүүхдийн тэтгэлэгтэй холбоотой торгосон дүн', 'type': 'number', 'unit': '₮', 'step': 'any'},
                {'id': 'oss_barivch',       'label': 'Баривчлах шийтгэл',                             'type': 'number', 'unit': 'хүн'},
            ]
        }
    ],

    # ── Бүс хариуцсан (өргөдөл/гомдол) ────────────────────────────────────
    'bus_orgodol': [
        {
            'title': 'Өргөдөл, гомдол',
            'fields': [
                {'id': 'khulEen_avsan',     'label': 'Хүлээн авсан',             'type': 'number', 'unit': 'ш'},
                {'id': 'shiydsersen',       'label': 'Шийдвэрлэсэн',             'type': 'number', 'unit': 'ш'},
                {'id': 'khyanagdaj_baina',  'label': 'Хянагдаж байгаа',          'type': 'number', 'unit': 'ш'},
                {'id': 'undesleltei',       'label': 'Үндэслэлтэй',              'type': 'number', 'unit': 'ш'},
                {'id': 'undeslelnugui',     'label': 'Үндэслэлгүй',              'type': 'number', 'unit': 'ш'},
                {'id': 'uurg_yavuulsan',    'label': 'Явуулсан үүрэг',           'type': 'textarea'},
                {'id': 'arga_hemjee',       'label': 'Арга хэмжээ тооцох санал', 'type': 'textarea'},
            ]
        }
    ],

    # ── Бүсийн нэгтгэгч (Г.Алтансувд — system нэгтгэхэд шаардлагагүй болно) ─
    'negtle_bus': [
        {
            'title': 'Бүсийн нэгтгэл (өргөдөл, гомдол)',
            'note': 'Системд бүсийн нийлбэр автоматаар гарна. Нэмэлт тайлбар оруулж болно.',
            'fields': [
                {'id': 'negtle_tailbar', 'label': 'Нэмэлт тайлбар / тэмдэглэл', 'type': 'textarea'},
            ]
        }
    ],

    # ── Цахим бүртгэл ────────────────────────────────────────────────────────
    'tsakhim': [
        {
            'title': 'Тээврийн хэрэгсэл',
            'fields': [
                {'id': 'erh_tudgeljuulsen',  'label': 'Захиран зарцуулах эрх түдгэлзүүлсэн', 'type': 'number', 'unit': 'ш'},
                {'id': 'erh_sergeesan',      'label': 'Эрхийг сэргээсэн',                   'type': 'number', 'unit': 'ш'},
            ]
        },
        {
            'title': 'Цахим сан',
            'fields': [
                {'id': 'zasvarласан_barimt',  'label': 'Зөрүүтэй бүртгэлийг засварласан гүйцэтгэх баримт бичиг', 'type': 'number', 'unit': 'ш'},
                {'id': 'eren_niit',            'label': 'Эрэн сурвалжлагдаж байгаа нийт тоо',                  'type': 'number', 'unit': 'хүн'},
                {'id': 'khaяg_togtosson',      'label': 'Оршин суух хаяг олж тогтоосон',                       'type': 'number', 'unit': 'хүн'},
            ]
        }
    ],

    # ── Хилийн хориг ─────────────────────────────────────────────────────────
    'hil': [
        {
            'title': 'Гадаадад зорчих эрх',
            'fields': [
                {'id': 'hil_tudgeljuulsen',  'label': 'Гадаадад зорчих эрх түдгэлзүүлсэн',  'type': 'number', 'unit': 'хүн'},
                {'id': 'hil_sergeesan',      'label': 'Гадаадад зорчих эрх сэргээсэн',       'type': 'number', 'unit': 'хүн'},
                {'id': 'hil_tolgoi_dun',     'label': 'Барагдуулсан мөнгөн дүн',             'type': 'number', 'unit': '₮', 'step': 'any'},
            ]
        }
    ],

    # ── Мэдээ, дүн шинжилгээ (Э.Ганчимэг) ──────────────────────────────────
    'medee_too': [
        {
            'title': 'Гүйцэтгэх баримт бичгийн биелэлт',
            'table': True,
            'categories': [
                'Иргэний хэрэг',
                'Эрүүгийн хэрэг',
                'Захиргааны хэрэг',
                'Зөрчлийн шийдвэр гүйцэтгэл',
                'Бусад хэрэг',
                'Хүүхдийн тэтгэлэг',
                'Нэгдсэн мэдээ',
            ],
            'cols': [
                {'id': 'bieluu_too',  'label': 'Биелүүлбэл зохих тоо',    'unit': 'ш'},
                {'id': 'bieluu_dun',  'label': 'Биелүүлбэл зохих дүн',    'unit': '₮'},
                {'id': 'bodit_too',   'label': 'Бодитой биелүүлсэн тоо',  'unit': 'ш'},
                {'id': 'bodit_dun',   'label': 'Бодитой биелүүлсэн дүн',  'unit': '₮'},
                {'id': 'uldegdel_too','label': 'Үлдэгдэл тоо',            'unit': 'ш'},
                {'id': 'uldegdel_dun','label': 'Үлдэгдэл дүн',            'unit': '₮'},
                {'id': 'bodit_pct',   'label': 'Бодит биелэлт',           'unit': '%'},
                {'id': 'mongon_pct',  'label': 'Мөнгөн дүн биелэлт',      'unit': '%'},
            ]
        },
        {
            'title': 'Нэмэлт мэдээлэл',
            'fields': [
                {'id': 'shine_barimt',      'label': 'Шүүхээс шинээр нэмэгдсэн гүйцэтгэх баримт бичиг', 'type': 'number', 'unit': 'ш'},
                {'id': 'tetgleg_huukhed',   'label': 'Тэтгэлэг авагч хүүхдийн нийт тоо',                'type': 'number', 'unit': 'хүүхэд'},
                {'id': 'tetgleg_0_11',      'label': '0-11 насны хүүхэд',                               'type': 'number', 'unit': 'хүүхэд'},
                {'id': 'tetgleg_11plus',    'label': '11+ насны хүүхэд',                                'type': 'number', 'unit': 'хүүхэд'},
            ]
        }
    ],

    # ── Шүүхийн нэхэмжлэл (Ц.Үдвал) ────────────────────────────────────────
    'nekhemjlel': [
        {
            'title': 'Тухайн 7 хоногт — шүүхэд хариуцагчаар татагдсан',
            'fields': [
                {'id': 'niit_nekhemjlel',    'label': 'Нийт нэхэмжлэл',           'type': 'number', 'unit': 'ш'},
                {'id': 'toloгч_ees',         'label': 'Төлбөр төлөгчөөс',         'type': 'number', 'unit': 'ш'},
                {'id': 'avagch_ees',         'label': 'Төлбөр авагчаас',           'type': 'number', 'unit': 'ш'},
                {'id': 'guravdagch',         'label': 'Гуравдагч этгээдээс',       'type': 'number', 'unit': 'ш'},
                {'id': 'etsesen_shiydsersen','label': 'Эцэслэн шийдвэрлэсэн',      'type': 'number', 'unit': 'ш'},
                {'id': 'heregsekhgui',       'label': '— Хэрэгсэхгүй болгосон',    'type': 'number', 'unit': 'ш'},
            ]
        },
        {
            'title': 'Хяналтад байгаа нэхэмжлэл (агуулгаар)',
            'fields': [
                {'id': 'hyan_duudlaga',      'label': 'Дуудлага худалдаа хүчингүй болгох', 'type': 'number', 'unit': 'ш'},
                {'id': 'hyan_unelgee',       'label': 'Үнэлгээ хүчингүй болгох',           'type': 'number', 'unit': 'ш'},
                {'id': 'hyan_hil',           'label': 'Хилийн хоригтой холбоотой',          'type': 'number', 'unit': 'ш'},
                {'id': 'hyan_busad',         'label': 'Бусад асуудлаар',                    'type': 'number', 'unit': 'ш'},
                {'id': 'hyan_niit',          'label': 'Нийт хяналтад байгаа',              'type': 'number', 'unit': 'ш'},
            ]
        },
        {
            'title': 'Өссөн дүнгээр',
            'fields': [
                {'id': 'oss_niit',           'label': 'Нийт нэхэмжлэл',           'type': 'number', 'unit': 'ш'},
                {'id': 'oss_toloгч',         'label': 'Төлбөр төлөгчөөс',         'type': 'number', 'unit': 'ш'},
                {'id': 'oss_avagch',         'label': 'Төлбөр авагчаас',           'type': 'number', 'unit': 'ш'},
                {'id': 'oss_guravdagch',     'label': 'Гуравдагч этгээдээс',       'type': 'number', 'unit': 'ш'},
                {'id': 'oss_etsesen',        'label': 'Эцэслэн шийдвэрлэсэн',      'type': 'number', 'unit': 'ш'},
            ]
        }
    ],

    # ── Өр төлбөргүй лавлагаа (З.Номин-Эрдэнэ) ──────────────────────────────
    'lavlagaa_negtle': [
        {
            'title': 'Лавлагаа олгосон',
            'fields': [
                {'id': 'lav_niit',           'label': 'Нийт олгосон лавлагаа',                   'type': 'number', 'unit': 'ш'},
                {'id': 'lav_tsakhim_shуudан','label': 'Цахим шуудангаар ирсэн хүсэлт',           'type': 'number', 'unit': 'ш'},
                {'id': 'lav_tulgaj',         'label': 'Цахим сантай тулгаж мэдээлэл хүргүүлсэн', 'type': 'number', 'unit': 'ш'},
                {'id': 'lav_irgend',         'label': 'Иргэнд цахимаас шалгаж хариу өгсөн',      'type': 'number', 'unit': 'ш'},
                {'id': 'lav_tailbar',        'label': 'Нэмэлт тайлбар',                          'type': 'textarea'},
            ]
        }
    ],

    # ── Өргөдөл, гомдол (Ч.Элбэг — төв) ────────────────────────────────────
    'orgodol_central': [
        {
            'title': 'Тухайн 7 хоногт',
            'fields': [
                {'id': 'org_irsen_niit',     'label': 'Нийт ирсэн өргөдөл, гомдол',       'type': 'number', 'unit': 'ш'},
                {'id': 'org_shiydsersen_tot', 'label': 'Шийдвэрлэж хариу өгсөн нийт',     'type': 'number', 'unit': 'ш'},
                {'id': 'org_shiydsersen_tolot','label': '— Төлбөр төлөгчөөс',              'type': 'number', 'unit': 'ш'},
                {'id': 'org_shiydsersen_avagch','label':'— Төлбөр авагчаас',               'type': 'number', 'unit': 'ш'},
                {'id': 'org_khyanagdaj',     'label': 'Хянагдаж байгаа',                  'type': 'number', 'unit': 'ш'},
                {'id': 'org_tatan_hyanaJ',   'label': 'Татан хянасан гүйцэтгэх баримт бичиг','type':'number','unit':'ш'},
            ]
        },
        {
            'title': 'ШШГЕГ-т хандсан',
            'fields': [
                {'id': 'shsgeg_avagch',      'label': 'Төлбөр авагчаас',    'type': 'number', 'unit': 'ш'},
                {'id': 'shsgeg_toloгч',      'label': 'Төлбөр төлөгчөөс',   'type': 'number', 'unit': 'ш'},
                {'id': 'shsgeg_undeslelnugui','label': 'Үндэслэлгүй',        'type': 'number', 'unit': 'ш'},
            ]
        },
        {
            'title': 'Шийдвэр гүйцэтгэх алба',
            'fields': [
                {'id': 'sga_avagch',         'label': 'Төлбөр авагчаас',    'type': 'number', 'unit': 'ш'},
                {'id': 'sga_toloгч',         'label': 'Төлбөр төлөгчөөс',   'type': 'number', 'unit': 'ш'},
                {'id': 'sga_undesleltei',    'label': 'Үндэслэлтэй',        'type': 'number', 'unit': 'ш'},
                {'id': 'sga_undeslelnugui',  'label': 'Үндэслэлгүй',        'type': 'number', 'unit': 'ш'},
            ]
        },
        {
            'title': 'Засгийн газрын 11-11 төв',
            'fields': [
                {'id': 'g1111_avagch',       'label': 'Төлбөр авагчаас',    'type': 'number', 'unit': 'ш'},
                {'id': 'g1111_toloгч',       'label': 'Төлбөр төлөгчөөс',   'type': 'number', 'unit': 'ш'},
                {'id': 'g1111_undesleltei',  'label': 'Үндэслэлтэй',        'type': 'number', 'unit': 'ш'},
                {'id': 'g1111_undeslelnugui','label': 'Үндэслэлгүй',        'type': 'number', 'unit': 'ш'},
            ]
        },
        {
            'title': 'Хууль зүй, дотоод хэргийн яам',
            'fields': [
                {'id': 'hzdhy_avagch',       'label': 'Төлбөр авагчаас',    'type': 'number', 'unit': 'ш'},
            ]
        },
        {
            'title': 'Даалгавар, шилжүүлэлт',
            'fields': [
                {'id': 'daalgavar_huрgуulsan','label': 'Гүйцэтгүүлэхээр хүргүүлсэн даалгавар', 'type': 'number', 'unit': 'ш'},
                {'id': 'daalgavar_guitsetgesen','label': 'Гүйцэтгэсэн даалгавар',               'type': 'number', 'unit': 'ш'},
                {'id': 'shiljuulsen_barimt',  'label': 'Шилжүүлсэн гүйцэтгэх баримт бичиг',   'type': 'number', 'unit': 'ш'},
            ]
        }
    ],

    # ── Дотоод ажил, хүний нөөц (Д.Намуун, М.Март) ─────────────────────────
    'dotood_ajil': [],   # General only (хийсэн/хийх)

    # ── Сургалт (Θ.Саруултуяа) ──────────────────────────────────────────────
    'surgalt': [],       # General only

    # ── Нэгтгэгч (Б.Золжаргал) ──────────────────────────────────────────────
    'negtle_main': [],   # General + review access

    # ── Дарга ────────────────────────────────────────────────────────────────
    'head': [],          # Review only
}


def get_user_form(user):
    role = user.get('role', '')
    return {
        'role':     role,
        'label':    ROLE_LABELS.get(role, role),
        'sections': ROLE_FORMS.get(role, []),
        'is_head':  role == 'head',
        'is_negtle': role in ('negtle_main', 'lavlagaa_negtle'),
    }
