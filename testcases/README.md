# Bo testcase bai Dia chi IP

Dap an (`.out`) sinh boi `ip_bruteforce.py` (duyet 3 vi tri cat, doc lap voi thuat toan quay lui). Thu tu dong trong `.out` da sap xep, khi so sanh can sap xep ket qua.

| Nhom | Ten | Do dai | So dap an | Khop brute force | Ghi chu |
|---|---|---|---|---|---|
| sample | sample_de_bai | 11 | 2 | OK | Vi du trong de wecode |
| normal | normal_01 | 12 | 0 | OK | 12 chu so nhung doan 001 co so 0 dau, vo nghiem |
| normal | normal_02 | 7 | 11 | OK | 7 chu so, nhieu dap an |
| normal | normal_03 | 6 | 5 | OK | Ket qua gom nhieu dia chi |
| normal | normal_04 | 6 | 9 | OK | 6 chu so |
| normal | normal_05 | 9 | 1 | OK | 9 chu so |
| boundary | edge_min_len_4 | 4 | 1 | OK | Do dai toi thieu de co nghiem: 4 |
| boundary | edge_max_len_12 | 12 | 1 | OK | Do dai toi da co nghiem: 12, dung 1 cach |
| boundary | edge_len_13 | 13 | 0 | OK | 13 chu so, vo nghiem |
| boundary | edge_len_3 | 3 | 0 | OK | 3 chu so, vo nghiem |
| boundary | edge_len_1 | 1 | 0 | OK | 1 chu so, vo nghiem |
| boundary | edge_all_zero_4 | 4 | 1 | OK | Chi co 0.0.0.0 |
| boundary | edge_all_zero_12 | 12 | 0 | OK | Vo nghiem vi so 0 dau |
| boundary | edge_255_max | 12 | 1 | OK | Moi doan = 255 |
| boundary | edge_256 | 12 | 0 | OK | Moi doan 256 > 255, vo nghiem |
| special | special_leading_zero_1 | 6 | 2 | OK | So 0 dung dau doan nhieu chu so |
| special | special_leading_zero_2 | 4 | 1 | OK | Chi 0.1.0.0 |
| special | special_leading_zero_3 | 5 | 0 | OK | 0 dau, nhieu so 0 |
| special | special_one_way_12 | 12 | 1 | OK | 12 chu so 1, dung 1 cach 111.111.111.111 |
| special | special_many_answers | 7 | 16 | OK | 7 chu so 1, nhieu dap an |
| special | special_digits_10 | 10 | 0 | OK | 10 chu so |
| special | special_255_mixed | 10 | 4 | OK | Gia tri sat 255 |
| invalid | invalid_letters | 5 | 0 | OK | Co ky tu khong phai so |
| invalid | invalid_empty | 0 | 0 | OK | Chuoi rong |
| random | random_01 | 9 | 0 | OK | Ngau nhien do dai 9 |
| random | random_02 | 9 | 0 | OK | Ngau nhien do dai 9 |
| random | random_03 | 4 | 1 | OK | Ngau nhien do dai 4 |
| random | random_04 | 4 | 1 | OK | Ngau nhien do dai 4 |
| random | random_05 | 7 | 6 | OK | Ngau nhien do dai 7 |
| random | random_06 | 4 | 1 | OK | Ngau nhien do dai 4 |
| random | random_07 | 4 | 1 | OK | Ngau nhien do dai 4 |
| random | random_08 | 9 | 0 | OK | Ngau nhien do dai 9 |
| random | random_09 | 5 | 4 | OK | Ngau nhien do dai 5 |
| random | random_10 | 4 | 1 | OK | Ngau nhien do dai 4 |
| random | random_11 | 9 | 0 | OK | Ngau nhien do dai 9 |
| random | random_12 | 8 | 6 | OK | Ngau nhien do dai 8 |
| random | random_13 | 11 | 2 | OK | Ngau nhien do dai 11 |
| random | random_14 | 8 | 3 | OK | Ngau nhien do dai 8 |
| random | random_15 | 8 | 5 | OK | Ngau nhien do dai 8 |
| random | random_small_alpha_01 | 10 | 5 | OK | Ngau nhien bang chu so 0125, do dai 10 |
| random | random_small_alpha_02 | 4 | 1 | OK | Ngau nhien bang chu so 0125, do dai 4 |
| random | random_small_alpha_03 | 12 | 0 | OK | Ngau nhien bang chu so 0125, do dai 12 |
| random | random_small_alpha_04 | 6 | 5 | OK | Ngau nhien bang chu so 0125, do dai 6 |
| random | random_small_alpha_05 | 8 | 12 | OK | Ngau nhien bang chu so 0125, do dai 8 |
| large | large_100_ones | 100 | 0 | OK | 100 chu so, vo nghiem, kiem tra cat tia |
| large | large_100_random | 100 | 0 | OK | 100 chu so ngau nhien |
| large | large_100_zeros | 100 | 0 | OK | 100 so 0 |
| large | large_13_ones | 13 | 0 | OK | 13 chu so, vuot 12 |
