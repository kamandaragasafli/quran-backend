"""Tətbiqdəki ilkin mətnlər — AppContent seed."""

from __future__ import annotations

ABOUT_DEFAULT = {
    'title': 'Miras Akademiyası',
    'lead': (
        'Quran müəllimlərinin və öyrənməyə əzm və səylə yanaşan tələbələrin ehtiyaclarını '
        'nəzərə alaraq hazırlanmış bir layihə.'
    ),
    'body': (
        'Quran Akademiyası olaraq həm Quran müəllimlərinin, həm də öyrənməyə əzm və səylə '
        'yanaşan tələbələrin ehtiyaclarını nəzərə alaraq, bugünün tələblərinə cavab verən və '
        'gələcəyin Quran tədrisinə təməl ola biləcək fərqli bir layihə ortaya qoymağa çalışırıq.\n\n'
        'Bu layihədə mövcud Quran mobil tətbiqlərini təkrarlamaq əvəzinə, səbr, əzm və peşəkar '
        'müəllim müşahidəsi tələb edən sistemli bir tədris anlayışını ön plana çıxardıq. '
        'Çünki layihənin əsas mesajlarından biri budur:\n\n'
        '> Quran öyrənmək səbr, əzm və müəllim müşahidəsi tələb edir.\n\n'
        'Quran Akademiyası qari dinləməkdə sərbəst seçim təqdim etmək əvəzinə, tələbəni doğru '
        'seçimə istiqamətləndirməyə üstünlük verir. Bu səbəbdən ilkin, orta və peşəkar '
        'səviyyələr üçün uyğun qarilər müəyyənləşdirilir və tələbəyə inkişaf mərhələsinə uyğun '
        'dinləmə istiqaməti təqdim olunur.\n\n'
        'Məqsədimiz istifadəçiyə geniş seçim imkanı vermək əvəzinə doğru seçimi göstərməkdir.\n\n'
        'Bununla layihənin işin əhli olan şəxslərin təcrübəsi əsasında hazırlandığını və hər '
        'mərhələdə tələbəni doğru istiqamətə yönəldən bir tədris bələdçisi olduğunu hiss '
        'etdirmək istəyirik.\n\n'
        'Quran Akademiyası sadəcə Quran dinləmək üçün hazırlanmış bir platforma deyil; '
        'müəllimin rolunu qoruyan, tələbənin mərhələli inkişafını əsas götürən və '
        'texnologiyanı Quran tədrisinə xidmət edən bir vasitəyə çevirən layihədir.\n\n'
        '## Miras Akademiyasında ilkin mərhələ nədir?\n\n'
        'Miras Akademiyasında “ilkin mərhələ” dedikdə əlifba səviyyəsi nəzərdə tutulmur. Burada '
        'müxtəsər təcvid elminin həm nəzəri, həm də praktiki yönünü mənimsəmiş şəxslər nəzərdə '
        'tutulur.\n\n'
        'Təcvidi bilməyən, zəif bilən və ya nəzəri qaydaları bildiyi halda onları praktik '
        'tilavətdə tətbiq etməkdə çətinlik çəkən şəxslər üçün mobil tətbiqimiz təkbaşına '
        'yetərli olmayacaq. Belə tələbələrin ilk növbədə ilkin səviyyə üzrə tələbə hazırlayan '
        'təcrübəli Quran müəlliminə müraciət etmələri tövsiyə olunur. Təcvidin nəzəri və '
        'praktiki təməli formalaşdıqdan sonra isə layihəmizin təqdim etdiyi qari siyahısından və '
        'digər təlim materiallarından mərhələli şəkildə faydalana bilərlər.\n\n'
        '## Hafizlər üçün fərqli təkrar metodikası\n\n'
        'Layihəmizin əsas hədəf qruplarından biri də hafizlik etdikdən sonra əzbəri zəifləyən, '
        'klassik təkrar üsulu ilə davam etməkdə çətinlik çəkən və Quranı daha praktik, maraqlı, '
        'özünü sınağa əsaslanan bir metodika ilə təkrar etmək istəyən hafizlərdir.\n\n'
        'Bu məqsədlə təqdim etdiyimiz üç fərqli səviyyədən ibarət hərəkəsiz Quran nəşri '
        'hafizlərin öz əzbər səviyyələrini yoxlamasına imkan verir.\n\n'
        '## Vəqf və ibtidə dəstəyi\n\n'
        'Vəqf və ibtidə elmi Quran elmləri arasında, xüsusilə praktiki yönü etibarilə mühüm yer '
        'tutur. İstər hafizlərin, istərsə də təcvidi bilən, lakin hafiz olmayan oxucuların '
        'tilavətdə ən çox çətinlik çəkdikləri mövzulardan biri harada dayanmaq və haradan '
        'başlamaq məsələsidir.\n\n'
        'Biz Miras Akademiyası olaraq bunu da nəzərə aldıq. Mushafdakı Səcavənd vəqf '
        'işarələri ilə kifayətlənməyərək müəyyən mövqelərə dəstəkləyici vəqf işarələri əlavə '
        'etdik.\n\n'
        'Miras Akademiyasının məqsədi də məhz budur: Quran öyrənmə prosesində müəllimi əvəz '
        'etmək deyil, müəllimdən gələn elmi mirası müasir vasitələrlə daha əlçatan, sistemli və '
        'praktik hala gətirmək.\n\n'
        '## Miras Akademiyası — Layihə Komandası\n\n'
        'Layihənin ideya müəllifi və elmi rəhbəri: Yunus Əlihüseynli\n\n'
        'İdeya · Elmi rəhbərlik · Metodika · Ümumi nəzarət\n\n'
        'Miras Akademiyasının ümumi konsepsiyası, layihənin işləmə prinsipi və inkişaf '
        'istiqamətləri Yunus Əlihüseynli tərəfindən müəyyən edilmişdir. Layihə çərçivəsində '
        'təqdim olunan elmi materialların hazırlanması və yoxlanılması, tədris metodikasının '
        'qurulması, Quran tilavəti üzrə mərhələlərin müəyyənləşdirilməsi, qari seçimləri, '
        'vəqf–ibtidā və istināf nöqtələrinin təyin edilməsi, eləcə də tətbiqin elmi istiqamətinə '
        'dair bütün qərarlar onun rəhbərliyi və nəzarəti altında həyata keçirilib.'
    ),
}

MEAL_INTRO_DEFAULT = {
    'title': 'Məna yönlü öyrənmə',
    'lead': (
        'Mövzuları ayə aralıqları ilə yadda saxlamaq və sistemli təkrar etmək üçün qısa bələdçi.'
    ),
    'body': (
        'Qurani-Kərimin ərəbcə mətnini əzbərləmək və təkrarlamaq üçün müəyyən metodlar olduğu kimi, '
        'mənanı öyrənmək, anlamaq və yadda saxlamaq üçün də sistemli şəkildə təkrar metodları mövcuddur.\n\n'
        'Biz bu bölümdə məna yönlü öyrənməni daha praktik hala gətirərək, mövzuların hansı surə və '
        'ayələrdə keçdiyini daha tez xatırlamağa və öyrənilənləri sistemli şəkildə təkrarlamağa '
        'kömək edən bir metod təqdim edirik.\n\n'
        'Qurani-Kərimdə mövzu keçidlərini və müəyyən hissələrin tamamlanmasını göstərmək üçün '
        'Mədinə nüsxələrində ◇ işarəsinə bənzər müxtəlif işarələrdən istifadə olunur. Bu işarələrin '
        'forması nüsxələrə görə dəyişə bilər. Türkiyədə çap olunan bəzi nüsxələrdə isə “rüku” '
        'sözündən ilhamlanaraq onun son hərfi olan ع (ayn) işarəsi qoyulur.\n\n'
        'Bu bölgülərin əsas məqsədlərindən biri hafizlərə tilavət zamanı praktik istiqamət verməkdir. '
        'Xüsusilə təhəccüd namazlarında və Ramazan ayında təravih qıldırarkən hər rükətdə oxunacaq '
        'hissələri yenidən hesablamaq əvəzinə, hazır bölgülərdən istifadə etmək mümkündür.\n\n'
        'Təbii ki, Quranın mənasına bələd olan təcrübəli hafiz öz əzbər və təkrar sistemini də nəzərə '
        'alaraq bu bölgüləri fərqli şəkildə müəyyən edə bilər.\n\n'
        'Biz də bu bölmələri hazırlayarkən qədim Mədinə nüsxələrindəki bölgüləri əsas götürdük, '
        'eyni zamanda məna və mövzu baxımından faydalı hesab etdiyimiz məqamları nəzərə alaraq '
        'bəzi yerlərdə öz bölgümüzü tətbiq etdik.\n\n'
        'Tətbiqdə isə ayrıca işarələrdən istifadə etmək əvəzinə, bölgülərin daha asan yadda qalması '
        'və təkrar zamanı praktik olması üçün ayə rəqəmlərinə üstünlük verdik.'
    ),
    'exampleLabel': 'Nümunə',
    'exampleRange': '1–24 | 25–36 | 37–44',
    'exampleHint': (
        'Beləliklə, istifadəçi (məal xülasəsini oxuyarkən) mövzunun hansı ayədə başlayıb, '
        'hansı ayədə tamamlandığını birbaşa ayə nömrələri üzərindən yadda saxlaya və həmin '
        'hissəni rahat şəkildə təkrar edə bilər.'
    ),
}

RECITERS_DEFAULT = {
    'intro': '',
    'guides': [
        {
            'reciterId': 'husary_muallim',
            'label': 'Mahmud Xəlil əl-Husari — Təlim qiraəti • 1-ci mərhələ',
            'level': 'talim',
            'style': '',
            'note': (
                'Husarinin təlim qiraəti praktiki təcvid məşqləri üçün ən uyğun nümunələrdən biridir. '
                'Aydın tələffüzü, məxrəc və sifətlərin qorunması, mədd miqdarları və təcvid hökmlərinin '
                'aydın tətbiqi tələbəyə nəzəri olaraq öyrəndiklərini tilavət üzərində eşidib müşahidə '
                'etmək imkanı verir.\n\n'
                'Burada məqsəd qarinin səsini və avazını təqlid etmək deyil. Məqsəd öyrənilmiş '
                'qaydaların düzgün tətbiqini eşitmək, fərqləndirmək və praktiki oxunuşda '
                'möhkəmləndirməkdir.\n\n'
                'Qeyd: Qari dinləmək ayrıca təlim metodu deyil, praktiki təlimi dəstəkləyən vasitədir. '
                'Hansı qarinin və hansı mərhələdə dinlənilməsi tələbənin səviyyəsinə uyğun müəyyən '
                'edilməlidir.'
            ),
            'tips': (
                'Öyrənilmiş məxrəc, sifət və təcvid hökmlərini praktikada müşahidə etmək üçün;\n'
                'Üzdən oxunuş zamanı öz tətbiqini düzgün nümunə ilə müqayisə etmək üçün;\n'
                'Təshih edilən xətanın doğru tətbiqini yenidən eşidib möhkəmləndirmək üçün;\n'
                'Hifz zamanı ayələrin düzgün oxunuşunu dəqiqləşdirmək və əzbəri möhkəmləndirmək üçün.'
            ),
            'closing': '',
        },
        {
            'reciterId': 'husary',
            'label': 'Mahmud Xəlil əl-Husari Təlim qiraəti • 2-ci mərhələ.',
            'level': 'talim',
            'style': 'Axıcı oxunuş və avaz məşqi',
            'note': (
                'Bu mərhələdə əsas təcvid tətbiqləri üzərində ilkin məşqlər tamamlanmış olur. '
                'Tələbə artıq diqqətini yalnız hərf və hökmlərin düzgün tətbiqinə deyil, oxunuşun '
                'axıcılığına, səsin idarəsinə və sadə avazın formalaşdırılmasına yönəldir.\n\n'
                'Husarinin 2-ci təlim tilavəti təcvid dəqiqliyini qoruyaraq səsə nəzarət etməyi, '
                'oxunuşun tempini sabit saxlamağı və avazı təbii şəkildə tilavətə daxil etməyi '
                'məşq etmək üçün uyğundur.'
            ),
            'tips': (
                'İlkin praktiki təcvid məşqlərindən sonra;\n'
                'Axıcı və sabit oxunuş üzərində çalışarkən;\n'
                'Səs idarəsini inkişaf etdirmək üçün;\n'
                'Sadə və təbii avaz üzərində məşq edərkən.'
            ),
            'closing': (
                'Bu mərhələdə məqsəd gözəl səs nümayiş etdirmək deyil; düzgün oxunuşa səs və avaz '
                'baxımından nizam qazandırmaqdır.'
            ),
        },
        {
            'reciterId': 'husary_broadcast',
            'label': 'Mahmud Xəlil əl-Husari — Təlim qiraəti • 3-cü mərhələ',
            'level': 'talim',
            'style': '',
            'note': (
                'Bu mərhələdə əvvəlki oxunuşlardan əsas fərq tempodur. Əvvəlki mərhələlərdə daha '
                'aşağı tempolu oxunuşlardan istifadə edilmişdi.\n\n'
                'Məqsəd tələbəni üç fərqli tempoda oxumağa alışdırmaq və tempo dəyişdikcə hərflərin '
                'məxrəc və sifətlərində, eləcə də hərəkələrə verilən səslərdə meydana gələn incə '
                'fərqləri praktik şəkildə müşahidə edib tətbiq edə bilməsini təmin etməkdir.\n\n'
                'Beləliklə, tələbə sadəcə sürəti artırmağı deyil, tempo dəyişsə belə təcvid '
                'keyfiyyətini və hərflərin düzgün tələffüzünü qorumağı öyrənir.'
            ),
            'tips': '',
            'closing': '',
        },
        {
            'reciterId': 'abdulbasit',
            'label': 'AbdulBəsit — 1-ci mərhələ',
            'level': 'ciddi',
            'style': '',
            'note': (
                'Bu mərhələdə tələbə artıq fərqli bir qulaq analizi qabiliyyətinə sahib olmalıdır.\n\n'
                'Əvvəlki mərhələlərdən fərqli olaraq burada avaz bir qədər ön plana çıxır. Bununla '
                'yanaşı, sürət, məxrəc və sifətlərin tətbiqi, hərəkələrə verilən səslər daha yumşaq '
                'və axıcı şəkildə davam edir.\n\n'
                'Bu mərhələni tilavət estetikasına keçidin ilkin mərhələsi adlandırmaq olar. Məqsəd '
                'sadəcə avazlı oxumaq deyil; təcvidin praktiki əsaslarını qoruyaraq səs və avazı '
                'tilavətə düzgün şəkildə daxil etməyi öyrənməkdir.\n\n'
                'Bu səbəbdən həmin mərhələdə müəllimin müşahidəsi, yönləndirməsi və məsləhəti böyük '
                'rol oynayır.'
            ),
            'tips': '',
            'closing': '',
        },
        {
            'reciterId': 'abdulbasit_mujawwad',
            'label': 'AbdulBəsit — 2-ci mərhələ',
            'level': 'ireli',
            'style': '',
            'note': (
                'Bu mərhələdə temp minimuma enir, kəlmələrə verilən məna vurğuları isə maksimum '
                'dərəcədə ön plana çıxır.\n\n'
                'Tələbə artıq təlimin son mərhələsindədir. Təcvidin nəzəri və praktiki yönlərini '
                'mənimsədikdən sonra əsas hədəf təcvid vurğuları ilə məna vurğularını bir-biri ilə '
                'sinxronlaşdırmaqdır.\n\n'
                'Yəni oxunuşda məxrəc, sifət, hərəkə, mədd və digər təcvid xüsusiyyətləri '
                'qorunmaqla yanaşı, ayənin mənası da səs və vurğular vasitəsilə hiss etdirilməlidir.\n\n'
                'Bu mərhələdə müəllimin müşahidəsi və yönləndirməsi xüsusi əhəmiyyət daşıyır.'
            ),
            'tips': '',
            'closing': '',
        },
        {
            'reciterId': 'ibrahim_akhdar',
            'label': 'İbrahim əl-Axdar',
            'level': 'mexrec',
            'style': '',
            'note': (
                'Mədinə məscidində — Allah Elçisinin (Allahın salavatı və salamı onun üzərinə olsun) '
                'məscidində — tədris əsasən müəyyən bir oxunuş üslubu üzərindən aparılır. Peşəkar '
                'oxucu olsan belə, onların tələb etdiyi üslubdan kənara çıxdıqda oxunuşun xətalı '
                'hesab edilə bilər.\n\n'
                'İbrahim əl-Əxdar bu məktəbin üslubunu təmsil edən qarilərdən biridir. Lakin onun '
                'oxunuşuna beynəlxalq səviyyədə təcrübəli bir oxucunun gözü ilə yanaşdıqda, qalın və '
                'incə hərflərin bir-birindən fərqləndirilməsində nəzərəçarpacaq dərəcədə ifrata '
                'varıldığı müşahidə olunur.\n\n'
                'Bu nümunənin təqdim edilməsində məqsəd həmin yanaşmanın tilavətə necə əks '
                'olunduğunu göstərmək, eyni zamanda dinləyiciləri fərqli tədris məktəblərinin '
                'mövcudluğu və onların tilavətə təsiri ilə tanış etməkdir.'
            ),
            'tips': '',
            'closing': '',
        },
        {
            'reciterId': 'banna',
            'label': 'Mahmud Əli əl-Bənnə',
            'level': 'xususi',
            'style': '',
            'note': (
                'Tələbədə məxrəc, sifət, qalın və incə hərflərin tələffüzü ilə bağlı müəyyən '
                'xətalar müşahidə olunduqda Mahmud Əli əl-Bənnənin tilavətlərindən nümunələr '
                'dinlədilməsi faydalı ola bilər.\n\n'
                'Məsələn, ط (ta) qalın hərfdir və qalqalə sifətinə malikdir. Bəzi tələbələrdə '
                'dilin sürüşməsi, məxrəcə və sifətə kifayət qədər diqqət edilməməsi səbəbilə ط '
                'hərfi sanki ona həms sifəti əlavə edilirmiş kimi tələffüz olunur.\n\n'
                'Mahmud Əli əl-Bənnənin bəzi oxunuşlarında da bu kimi tələffüz xüsusiyyətləri '
                'eşidilir. Buna görə onun tilavətindən müəyyən hissələr düzgün oxunuşa nümunə '
                'kimi deyil, xətanın praktik olaraq necə səsləndiyini tələbəyə hiss etdirmək və '
                'eşitmə yolu ilə fərqləndirmə bacarığını inkişaf etdirmək məqsədilə istifadə edilə bilər.'
            ),
            'tips': '',
            'closing': '',
        },
    ],
}


def default_for(key: str) -> dict:
    if key == 'about':
        return dict(ABOUT_DEFAULT)
    if key == 'meal_intro':
        return dict(MEAL_INTRO_DEFAULT)
    if key == 'reciters':
        return dict(RECITERS_DEFAULT)
    return {}
