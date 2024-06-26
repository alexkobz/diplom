Рассмотрим использование прилагательных и притяжательных местоимений перед словом «демократия» и результаты модели word2vec. Начнем с выступлений В. Путина и Д. Медведева. Президенты часто используют прилагательные «российская» и «наша» перед демократией, что показывает ориентированность президентов на отечественное развитие. Слова «прямая», «парламентская», «представительная», «электронная» говорят о том, что президентов волнуют институциональные вопросы. ![](https://github.com/alexkobz/diplom/blob/main/texts/president/president_adj.png) Что касается употребляемых в одном контексте слов, то ни одно не приковывает внимание, кроме слова «государственность». Это подтверждает то, о чем много говорилось в докладе – о видении демократии как «кирпича» в «здании» государственного управления.
| Слово | Значение |
| ----- | -------- |
| Демократический |	0,75 |
| Государственность | 0,53 |
| Народовластие | 0,50 |
| Цивилизованный | 0,48 |
| Многопартийность | 0,48 |
| Свобода |	0,47 |
| Идеология | 0,47 |
| Волеизъявление | 0,47 |
| Диктатура | 0,46 |
| Миропорядок |	0,46 |

Рассмотрим частоту употребления слова «демократия» на заседаниях Государственной Думы. ![](https://github.com/alexkobz/diplom/blob/main/texts/gosduma/%D0%9A%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D1%83%D0%BF%D0%BE%D0%BC%D0%B8%D0%BD%D0%B0%D0%BD%D0%B8%D0%B8%CC%86%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%20%D0%B4%D0%B5%D0%BC%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8%D1%8F%20%D0%93%D0%94.png) 
В течение 21 года депутаты парламента довольно часто и регулярно употребляли это слово. Однако не наблюдается четкого тренда, поэтому данные гистограммы не дают возможности сделать однозначных выводов о том, выросла или упала актуальность поднимаемых вопросов. Однако видно, что выделяется период 2006-2012 годы на фоне периодов 2000-2005 гг. и 2013-2021 гг.. Во многом употребление демократического лексикона в этот период носит, на наш взгляд, «ритуальный» характер. Это демонстрирует, например, всплеск использования в 2006 году на торжественном заседании 27 апреля по поводу 100-летия Государственной думы.  Относительная частота употребления прилагательных со словом «демократия» схожа с описанной выше частотой употребления президентами, что правдоподобно, судя по высокому государственному статусу. Однако также представлены слова «западный» и «американский», что отражает больший сдвиг в сторону внешнеполитических тем. ![](https://github.com/alexkobz/diplom/blob/main/texts/gosduma/gosduma_adj.png) Среди слов, близких по смыслу к слову «демократия», наибольший интерес вызывают слова «капитализм», «социализм», «буржуазный», «либерализм» и «коммунизм». Сложно ответить с полной уверенностью, почему именно эти слова оказались близкими, но выскажем предположение, что возможно это связано с актуальной для этого периода темой демократического транзита и переходного периода, именно поэтому часто споры о демократии велись в пространстве таких понятий из XX века, как «социализм» и «капитализм».
| Слово | Значение |
| ----- | -------- |
| Диктатура | 0,67 |
| Демократический | 0,63 |
| Коммунизм | 0,62 |
| Буржуазный | 0,62 |
| Социализм | 0,62 |
| Демократ | 0,61 |
| Либерализм | 0,61 |
| Капитализм | 0,60 |
| Цивилизованный | 0,60 |
| Завоевание | 0,58 |
                  
В газете «Известия» в связке со словом «демократия» часто используются слова, имеющие отношение как к институциональному развитию, так и к внешней политике. ![](https://github.com/alexkobz/diplom/blob/main/texts/izvestia/izvestia_adj.png) То же самое можно сказать с поправкой на небольшую разницу по частоте про такие газеты, как «Коммерсант», «Ведомости», «Независимая газета». ![](https://github.com/alexkobz/diplom/blob/main/texts/kommersant/kommersant_adj.png) ![](https://github.com/alexkobz/diplom/blob/main/texts/vedomosti/vedomosti_adj.png) ![](https://github.com/alexkobz/diplom/blob/main/texts/ng/ng_adj.png)Иначе выглядит использование прилагательных в газете «Взгляд», на радио «Эхо Москвы» и газете «Завтра». ![](https://github.com/alexkobz/diplom/blob/main/texts/vzglyad/vzglyad_adj.png) ![](https://github.com/alexkobz/diplom/blob/main/texts/echo/echo_adj.png) ![](https://github.com/alexkobz/diplom/blob/main/texts/zavtra/zavtra_adj.png)В этих СМИ преобладают такие прилагательные, как «западная», «американская», «европейская», что говорит о высокой доле внешнеполитического элемента. Говоря о семантической близости, для всех представленных СМИ демократия близка понятиям разных идеологий (либерализм, социализм) и строев (авторитаризм, тоталитаризм), что достаточно естественно. Однако не могут не обращать внимание два слова, свойственные только газете «Взгляд»: светоч и глобализм. Употребление редкого сочетания «светоч» и «демократия» говорит о язвительном тоне публикаций, а взаимосвязь между глобализмом и демократией напоминает об их обоюдных негативных последствиях. 
| Слово | Значение |
| ----- | -------- |
| Демократический |	0,67 |
| Либерализм | 0,66 |
| Диктатура | 0,64 | 
| Светоч | 0,63 |
| Тоталитаризм | 0,58 |
| Социализм | 0,56 |
| Свобода | 0,56 | 
| Автократия | 0,55 | 
| Капитализм | 0,55 |
| Глобализм | 0,55 | 

Также интересно то, что по результатам обучения модели на стенограммах радиостанции «Эха Москвы» высокий вес получили слова «авторитаризм», «диктатура», «тирания», «автократия, что демонстрирует озабоченность гостей радиостанции проблемами демократии в стране.

| Слово | Значение |
| ----- | -------- |
| Авторитаризм | 0,58 |
| Диктатура | 0,54 |
| Тирания | 0,52 |
| Либерализм | 0,52 |
| Народовластие | 0,52 |
| Демократический | 0,51 | 
| Автократия | 0,50 |
| Парламентаризм | 0,49 |
| Тоталитаризм | 0,47 | 
| Суверенный | 0,45 |      

В целом, на протяжении двадцати одного года красной линией тянутся два больших пункта. Первый – это демократический транзит. Участники дискуссии испытывают рефлексию по поводу перехода от советской системы к новой российской. Анализируемый дискурс был компонентом вопроса продолжавшегося постсоветского политического самоопределения, ответом на который практически у всех политических сил была демократия, хотя вкладывавшийся в это понятие смысл существенно разнился. Из этого происходит гипотеза молодости российской демократии, на что принято списывать несовершенства политической системы. Этот пункт ослабевает примерно к началу второго десятилетия, хотя и продолжает присутствовать. Второй пункт – это внешнеполитический фактор. Он, наоборот, набирает силу на протяжении всего обозреваемого периода и становится доминирующим.

К концу двадцати одного года представители власти сообщали об удовлетворительных итогах демократизации и даже полном утверждении демократии в России, оппозиция же придерживалась противоположной точки зрения. Также можно заметить, что с течением времени в дискурсе наблюдалось усиление «партии власти». Другие политические партии уступали, не сумев предложить повестку дня, которая была бы принята большинством общества. 
