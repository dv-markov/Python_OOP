# Заполнение склада

def fill_inventory():
    from SC_r1 import Body, Bonnet, Seat
    inv = list()

    # BODY EN DN50
    inv.append(Body('0100-8530', 'Корпус тип 3241 DN50 PN25-40 Исполнение F DIN (1.0619)', 50,
                    ('1.0619', 'A216 WCC')))
    inv.append(Body('0104-1246', 'Корпус тип 3241 DN50 PN25-40 Исполнение F DIN (1.5638)', 50,
                    ('1.5638', 'A352 LC3')))
    inv.append(Body('0103-6354', 'Корпус тип 3241 DN50 PN25-40 Исполнение F DIN (1.4408)', 50,
                    ('1.4408', 'A351 CF8M')))
    # BODY EN DN80
    inv.append(Body('00100-8560', 'Корпус тип 3241 DN80 PN25-40 Исполнение F DIN (1.0619)', 80,
                    ('1.0619', 'A216 WCC')))
    inv.append(Body('0104-1250', 'Корпус тип 3241 DN80 PN25-40 Исполнение F DIN (1.5638)', 80,
                    ('1.5638', 'A352 LC3')))
    inv.append(Body('0103-7430', 'Корпус тип 3241 DN80 PN25-40 Исполнение F DIN (1.4408)', 80,
                    ('1.4408', 'A351 CF8M')))
    # BODY RU DN50
    inv.append(Body('0100-8530-RU', 'Корпус тип 3241 DN50 PN25-40 Исполнение F ГОСТ (20ГЛ)', 50,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Body('0103-6354-RU', 'Корпус тип 3241 DN50 PN25-40 Исполнение F ГОСТ (12Х18Н9ТЛ)', 50,
                    ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # BODY RU DN80
    inv.append(Body('0100-8560-RU', 'Корпус тип 3241 DN80 PN25-40 Исполнение F ГОСТ (20ГЛ)', 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Body('0103-7430-RU', 'Корпус тип 3241 DN80 PN25-40 Исполнение F ГОСТ (12Х18Н9ТЛ)', 80,
                    ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))

    # BONNET EN DN32-40-50
    inv.append(Bonnet('1590-8445', 'Крышка тип 3241 DN32-50 (1.0460) с втулкой (1.4104)', (32, 40, 50),
                      ('20ГЛ', '1.0619', 'A216 WCC')))
    inv.append(Bonnet('1993-0739', 'Крышка тип 3241 DN32-50 (1.5638) с втулкой (1.4404)', (32, 40, 50),
                      ('20ГЛ', '1.5638', 'A352 LC3')))
    inv.append(Bonnet('1991-6457', 'Крышка тип 3241 DN32-50 (1.4404) с втулкой (1.4404)', (32, 40, 50),
                      ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # BONNET RU DN32-40-50
    inv.append(Bonnet('1590-8445-RU', 'Крышка тип 3241 DN32-50 (09Г2С) с втулкой (12Х17)', (32, 40, 50),
                      ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Bonnet('1991-6457-RU', 'Крышка тип 3241 DN32-50  (08Х18Н10Т) с втулкой (08Х17Н13М2Т)', (32, 40, 50),
                      ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # BONNET EN DN65-80
    inv.append(Bonnet('1590-8447', 'Крышка тип 3241 DN65-80 (1.0460) с втулкой (1.4104)', (65, 80),
                      ('20ГЛ', '1.0619', 'A216 WCC')))
    inv.append(Bonnet('1993-0741', 'Крышка тип 3241 DN65-80 (1.5638) с втулкой (1.4404)', (65, 80),
                      ('20ГЛ', '1.5638', 'A352 LC3')))
    inv.append(Bonnet('1991-7755', 'Крышка тип 3241 DN65-80 (1.4404) с втулкой (1.4404)', (65, 80),
                      ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # BONNET RU DN65-80
    inv.append(Bonnet('1590-8447-RU', 'Крышка тип 3241 DN65-80 (09Г2С) с втулкой (12Х17)', (65, 80),
                      ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Bonnet('1991-7755-RU', 'Крышка тип 3241 DN65-80 (08Х18Н10Т) с втулкой (08Х17Н13М2Т)', (65, 80),
                      ('12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))

    # SEAT EN DN32-40-50 Kvs25
    inv.append(Seat('0110-1798', 'Седло тип 3241 DN32-50 SB38 me (1.4006)', (32, 40, 50), 25,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7726', 'Седло тип 3241 DN32-50 SB38 me (1.4404)', (32, 40, 50), 25,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    inv.append(Seat('0110-2532', 'Седло тип 3241 DN32-50 SB38 st (1.4006)', (32, 40, 50), 25,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7733', 'Седло тип 3241 DN32-50 SB38 st (1.4404)', (32, 40, 50), 25,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # SEAT RU DN32-40-50 Kvs25
    inv.append(Seat('0111-4603-RU', 'Седло тип 3241 DN32-50 SB38 me (12Х13)', (32, 40, 50), 25,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0111-4602-RU', 'Седло тип 3241 DN32-50 SB38 me (08Х18Н10Т)', (32, 40, 50), 25,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    inv.append(Seat('0111-4597-RU', 'Седло тип 3241 DN32-50 SB38 st (12Х13)', (32, 40, 50), 25,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0111-5087-RU', 'Седло тип 3241 DN32-50 SB38 st (08Х18Н10Т)', (32, 40, 50), 25,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # SEAT EN DN32-40-50 Kvs40
    inv.append(Seat('0110-1799', 'Седло тип 3241 DN32-50 SB48 me (1.4006)', (32, 40, 50), 40,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7727', 'Седло тип 3241 DN32-50 SB48 me (1.4404)', (32, 40, 50), 40,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    inv.append(Seat('0110-2533', 'Седло тип 3241 DN32-50 SB48 st (1.4006)', (32, 40, 50), 40,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7734', 'Седло тип 3241 DN32-50 SB48 st (1.4404)', (32, 40, 50), 40,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # SEAT RU DN32-40-50 Kvs40
    inv.append(Seat('0111-5311-RU', 'Седло тип 3241 DN32-50 SB48 me (12Х13)', (32, 40, 50), 40,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0111-5310-RU', 'Седло тип 3241 DN32-50 SB48 me (08Х18Н10Т)', (32, 40, 50), 40,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    inv.append(Seat('0111-4609-RU', 'Седло тип 3241 DN32-50 SB48 st (12Х13)', (32, 40, 50), 40,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0111-4580-RU', 'Седло тип 3241 DN32-50 SB48 st (08Х18Н10Т)', (32, 40, 50), 40,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # SEAT EN DN65-80 Kvs60
    inv.append(Seat('0110-1805', 'Седло тип 3241 DN65-80 SB63 me (1.4006)', (65, 80), 60,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7742', 'Седло тип 3241 DN65-80 SB63 me (1.4404)', (65, 80), 60,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    inv.append(Seat('0110-2536', 'Седло тип 3241 DN65-80 SB63 st (1.4006)', (65, 80), 60,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7750', 'Седло тип 3241 DN65-80 SB63 st (1.4404)', (65, 80), 60,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # SEAT RU DN65-80 Kvs60
    inv.append(Seat('0110-7701-RU', 'Седло тип 3241 DN65-80 SB63 me (12Х13)', (65, 80), 60,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7696-RU', 'Седло тип 3241 DN65-80 SB63 me (08Х18Н10Т)', (65, 80), 60,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    inv.append(Seat('0111-1202-RU', 'Седло тип 3241 DN65-80 SB63 st (12Х13)', (65, 80), 60,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-0663-RU', 'Седло тип 3241 DN65-80 SB63 st (08Х18Н10Т)', (65, 80), 60,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # SEAT EN DN65-80 Kvs80
    inv.append(Seat('0110-1806', 'Седло тип 3241 DN65-80 SB80 me (1.4006)', (65, 80), 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7743', 'Седло тип 3241 DN65-80 SB80 me (1.4404)', (65, 80), 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    inv.append(Seat('0110-2537', 'Седло тип 3241 DN65-80 SB80 st (1.4006)', (65, 80), 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-7751', 'Седло тип 3241 DN65-80 SB80 st (1.4404)', (65, 80), 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    # SEAT RU DN65-80 Kvs80
    inv.append(Seat('0110-6809-RU', 'Седло тип 3241 DN65-80 SB80 me (12Х13)', (65, 80), 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0111-4607-RU', 'Седло тип 3241 DN65-80 SB80 me (08Х18Н10Т)', (65, 80), 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))
    inv.append(Seat('0111-3253-RU', 'Седло тип 3241 DN65-80 SB80 st (12Х13)', (65, 80), 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3')))
    inv.append(Seat('0110-9846-RU', 'Седло тип 3241 DN65-80 SB80 st (08Х18Н10Т)', (65, 80), 80,
                    ('20ГЛ', '1.0619', 'A216 WCC', '1.5638', 'A352 LC3', '12Х18Н9ТЛ', '1.4408', 'A351 CF8M')))

    return inv
