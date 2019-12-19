# Soal 1
# select * from city where countrycode = 'IDN' order by population desc limit 10;

# Soal 2
# mysql> select ID, city.name as nama_kota, District, country.name as negara, city.Population as population from
#     -> city inner join country
#     -> on city.countrycode = country.code
#     -> order by population desc
#     -> limit 10;

# Soal 3
# mysql> select code, name, continent, region, indepyear as tahun_merdeka from country
#     -> where indepyear is not null
#     -> order by tahun_merdeka
#     -> limit 10;

# Soal 4
