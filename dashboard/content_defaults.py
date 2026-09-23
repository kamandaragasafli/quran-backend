"""Tətbiqdəki ilkin mətnlər — AppContent seed."""

from __future__ import annotations

ABOUT_DEFAULT = {
    'title': 'Miras Akademiyası',
    'lead': (
        'Quran müəllimlərinin və öyrənməyə əzm və səylə yanaşan tələbələrin ehtiyaclarını '
        'nəzərə alaraq hazırlanmış bir layihə.'
    ),
    'body': (
        'Miras Akademiyası olaraq həm Quran müəllimlərinin, həm də öyrənməyə əzm və səylə '
        'yanaşan tələbələrin ehtiyaclarını nəzərə alaraq, bugünün tələblərinə cavab verən və '
        'gələcəyin Quran tədrisinə təməl ola biləcək fərqli bir layihə ortaya qoymağa çalışırıq.\n\n'
        'Bu layihədə mövcud Quran mobil tətbiqlərini təkrarlamaq əvəzinə, səbr, əzm və peşəkar '
        'müəllim müşahidəsi tələb edən sistemli bir tədris anlayışını ön plana çıxardıq. '
        'Çünki layihənin əsas mesajlarından biri budur:\n\n'
        '> Quran öyrənmək səbr, əzm və müəllim müşahidəsi tələb edir.\n\n'
        'Miras Akademiyası qari dinləməkdə sərbəst seçim təqdim etmək əvəzinə, tələbəni doğru '
        'seçimə istiqamətləndirməyə üstünlük verir. Bu səbəbdən ilkin, orta və peşəkar '
        'səviyyələr üçün uyğun qarilər müəyyənləşdirilir və tələbəyə inkişaf mərhələsinə uyğun '
        'dinləmə istiqaməti təqdim olunur.\n\n'
        'Məqsədimiz istifadəçiyə geniş seçim imkanı vermək əvəzinə doğru seçimi göstərməkdir.\n\n'
        'Bununla layihənin işin əhli olan şəxslərin təcrübəsi əsasında hazırlandığını və hər '
        'mərhələdə tələbəni doğru istiqamətə yönəldən bir tədris bələdçisi olduğunu hiss '
        'etdirmək istəyirik.\n\n'
        'Miras Akademiyası sadəcə Quran dinləmək üçün hazırlanmış bir platforma deyil; '
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


TELEGRAM_DEFAULT = {
    'url': 'https://t.me/mirasacademy_az114',
    'handle': 't.me/mirasacademy_az114',
    'channelLabel': 'Miras kanalı',
    'headline': 'MİRAS — elmi məlumatın praktik tilavətlə tamamlandığı platforma',
    'body': (
        'Miras mobil tətbiqində Quran tilavətinin müxtəlif mərhələlərinə aid elmi və metodiki '
        'qeydlər sistemli şəkildə təqdim olunur. Lakin tilavət yalnız oxumaqla mənimsənilən bir '
        'sahə deyil. Bəzi incəliklər yazı ilə izah edilsə də, onların mahiyyəti eşidildikdə və '
        'praktik nümunə üzərində göstərildikdə daha aydın anlaşılır.\n\n'
        'Məhz bu məqsədlə Miras Telegram kanalı mobil tətbiqin praktik tamamlayıcısı olaraq '
        'fəaliyyət göstərəcək.\n\n'
        'Tətbiqdə yer alan vəqf və istinəf nöqtələri, məna vurğuları, səs idarəsi, sadə avaz, '
        'təcvidin incəlikləri və hüsni-ədaya aid xüsusi qeydlər kanalda səsli nümunələr və '
        'praktiki tətbiqlərlə nümayiş etdiriləcək.\n\n'
        'Burada məqsəd yeni qaydalar toplusu yaratmaq deyil; öyrənilən elmin tilavətdə necə '
        'tətbiq olunduğunu göstərməkdir.'
    ),
    'pair': (
        'Mobil tətbiq — elmi istiqaməti göstərir.\n'
        'Telegram — onun praktik əksini eşitdirir.'
    ),
    'brand': 'MİRAS',
    'slogan': 'Oxumaq, anlamaq, eşitmək və tətbiq etmək.',
    'note': (
        'Bu variantda Telegram ayrıca layihə kimi deyil, mobil tətbiqin praktik təlim qolu '
        'kimi təqdim olunur.'
    ),
    'author': 'Yunus Əlihüseynli',
    'ctaLabel': 'Kanala keç',
}


PRIVACY_DEFAULT = {
    'title': 'Gizlilik siyasəti',
    'lead': (
        'Bu sənəd Miras Akademiyası mobil tətbiqinin («Miras», «tətbiq») şəxsi məlumatları '
        'necə topladığını, saxladığını və istifadə etdiyini izah edir. Tətbiqdən istifadə '
        'etməklə bu siyasətlə razılaşırsınız.'
    ),
    'body': (
        '## 1. Giriş\n\n'
        'Miras Akademiyası Quran tədrisi, tilavət, əzbərləmə və əlaqəli təlim materialları '
        'təqdim edən təhsil layihəsidir. Şəxsi məxfiliyinizə hörmət edirik və məlumatları '
        'yalnız xidmətin işləməsi üçün lazım olan həcmdə emal edirik.\n\n'
        '## 2. Hansı məlumatlar toplanır?\n\n'
        '### 2.1. Cihazda saxlanan məlumatlar\n\n'
        'Tətbiq oxuma rahatlığı üçün bəzi məlumatları cihazınızda (lokal yaddaşda) saxlaya bilər:\n\n'
        '- Son oxunan səhifə / surə və oxuma irəliləyişi\n'
        '- Əlfavoritlər, əzbər səviyyəsi və oxşar seçimlər\n'
        '- Tema, qari seçimi və digər tətbiq parametrləri\n'
        '- Offline keş (məzmun, audio və ya işarələr)\n\n'
        'Bu məlumatlar adətən hesab yaratmadan, birbaşa cihazınızda qalır.\n\n'
        '### 2.2. Serverə göndərilən məlumatlar\n\n'
        'Məzmun yeniləmələri, xülasələr, söz işarələri, chat və digər onlayn funksiyalar '
        'üçün tətbiq bizim serverlərimizə sorğu göndərə bilər. Bu zaman texniki jurnalda '
        'aşağıdakılar qeydə alına bilər:\n\n'
        '- IP ünvanı\n'
        '- Sorğu tarixi və vaxtı\n'
        '- Cihaz / brauzer tipi (User-Agent)\n'
        '- Sorğu edilən ünvan (API yolu)\n\n'
        'Biz sizin adınızı, telefon nömrənizi və ya e-poçtunuzu tətbiqin əsas oxuma '
        'funksiyası üçün tələb etmirik. Chat və ya digər əlavə xidmətlərdə özünüz '
        'paylaşdığınız məlumatlar həmin xidmətin məqsədinə uyğun emal oluna bilər.\n\n'
        '## 3. Məlumatların istifadə məqsədi\n\n'
        'Toplanan məlumatlar aşağıdakı məqsədlər üçün istifadə olunur:\n\n'
        '- Tətbiqin və məzmunun düzgün işləməsi\n'
        '- Oxuma təcrübəsinin fərdiləşdirilməsi (irəliləyiş, seçimlər)\n'
        '- Xətaların aşkarlanması və təhlükəsizliyin qorunması\n'
        '- Xidmətin təkmilləşdirilməsi\n\n'
        'Şəxsi məlumatlarınızı reklam üçün üçüncü şəxslərə satmırıq.\n\n'
        '## 4. Üçüncü tərəf xidmətləri\n\n'
        'Tətbiq bəzi hallarda üçüncü tərəf mənbələrdən audio, şrift və ya digər məzmun '
        'yükləyə bilər. Həmçinin Telegram kanalı və oxşar xarici keçidlər açıla bilər. '
        'Bu xidmətlərin öz gizlilik qaydaları vardır; onlardan istifadə etdiyiniz zaman '
        'həmin qaydalar da tətbiq olunur.\n\n'
        '## 5. Məlumatların saxlanması və təhlükəsizlik\n\n'
        'Lokal məlumatlar cihazınızın əməliyyat sistemi tərəfindən qorunur. Server '
        'jurnalları və məzmun məlumatları xidmətin işləməsi üçün lazım olan müddət '
        'saxlanıla bilər. Məlumatların qorunması üçün ağlabatan texniki və təşkilati '
        'tədbirlər görürük; lakin internet üzərindən ötürülmənin tam riskdən azad '
        'olduğuna zəmanət vermək mümkün deyil.\n\n'
        '## 6. Uşaqların məxfiliyi\n\n'
        'Tətbiq ümumi auditoriya, o cümlədən Quran tədrisi ilə məşğul olanlar üçündür. '
        '13 yaşdan kiçik uşaqlardan bilərəkdən şəxsi məlumat toplamırıq. Əgər belə '
        'məlumatın bizə çatdığını düşünürsinizsə, bizimlə əlaqə saxlayın — müvafiq '
        'məlumatı siləcəyik.\n\n'
        '## 7. Sizin hüquqlarınız\n\n'
        'Mövcud qanunvericilik çərçivəsində:\n\n'
        '- Cihaz parametrlərindən tətbiq məlumatlarını silə bilərsiniz '
        '(tətbiqi silmək və ya keşi təmizləmək)\n'
        '- Suallarınız və məlumatların silinməsi ilə bağlı sorğularınız üçün bizimlə '
        'əlaqə saxlaya bilərsiniz\n\n'
        '## 8. Siyasətin yenilənməsi\n\n'
        'Bu gizlilik siyasəti vaxtaşırı yenilənə bilər. Əhəmiyyətli dəyişikliklər '
        'tətbiqdə və ya idarə panelindəki bu səhifədə əks olunacaq. Yenilənmiş '
        'versiyanın dərcindən sonra tətbiqdən istifadə etməyə davam etməyiniz '
        'yenilənmiş siyasətlə razılaşmanız kimi qəbul edilə bilər.\n\n'
        '## 9. Əlaqə\n\n'
        'Gizlilik siyasəti barədə suallarınız üçün Miras Akademiyası ilə əlaqə saxlayın '
        '(tətbiqdəki Telegram / əlaqə kanalları vasitəsilə).\n\n'
        'Son yenilənmə: 2026.'
    ),
}


def default_for(key: str) -> dict:
    if key == 'about':
        return dict(ABOUT_DEFAULT)
    if key == 'privacy':
        return dict(PRIVACY_DEFAULT)
    if key == 'meal_intro':
        return dict(MEAL_INTRO_DEFAULT)
    if key == 'reciters':
        return dict(RECITERS_DEFAULT)
    if key == 'telegram':
        return dict(TELEGRAM_DEFAULT)
    return {}
