# BOS-dop
Дополнительное задание по безопасности операционных систем 
Выполнил студент группы Б18-505 Магоян Т.А.

## Опакечивание репозитория

Клионируем репозиторий
    git clone https://github.com/parazyd/git-restrict.git

Копируем папку репозитория в ~/rpmbuild/SOURCES/
    cp -r git-restrict/ rpmbuild/SOURCES/

Переименовываем 
    mv git-restrict git-restrict-1.0

Архивируем 
    tar cvfz git-restrict-1.0.tar.gz git-restrict-1.0

## Заполнение spec файла

Переходим в папку ~/rpmbuild/SPECS и создаем файл git-restrict.spec
    vi git-restrict.spec

Запускаем сборку пакета
    rpmbuild -ba git-restrict.spec

## Подпись пакета

Генерируем gpg ключ
    gpg2 --gen-key

Экспортируем публичную часть ключа и сохраняем в файл
    gpg2 --export -a 'Magoyan Tigran' > ~/rpmbuild/RPM-GPG-KEY-Magoyan-Tigran

Создаем макрос, в который записываем %_gpg_name Magoyan Tigran
```
cd
vi .rpmmacros
```

Заходим в папку ~/rpmbuild/RPMS/x86_64/ и подписываем все пакеты
    rpm --addsign *.rpm
