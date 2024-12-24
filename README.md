# LibraryProject
Django Project
# Django Library Project

Ushbu loyiha Django yordamida yaratilgan kitoblar kutubxonasi boshqaruv tizimidir. Loyihada kitoblar, mualliflar, toifalar va foydalanuvchilar bilan bog'liq ma'lumotlarni saqlash va boshqarish uchun modellar qo'shildi.

## Asosiy Funksiyalar

1. **Admin Interface**:
   - Django admin interfeysi optimallashtirildi:
     - Modellar uchun maxsus oynalar yaratildi.
     - Fayllar uchun "image preview" funksiyasi qo'shildi.
     - Filtrlar va qidiruv maydonlari qo'shildi.

2. **Modellar**:
   - `Category`: Kitoblar toifalari haqida ma'lumot.
   - `Author`: Mualliflarning ma'lumotlarini boshqarish.
   - `Books`: Kitoblar bilan bog'liq barcha ma'lumotlar (narx, format, toifalar va boshqalar).
   - `Reviews`: Foydalanuvchilar tomonidan berilgan kitob sharhlari va baholari.

3. **Migration**:
   - Modellar database bilan muvaffaqiyatli integratsiya qilindi va migratsiya bajarildi.

## Loyiha O'rnatilishi

1. **Talablar**: Loyiha uchun kerakli Python kutubxonalarini o'rnatish uchun quyidagi buyruqdan foydalaning:

   ```bash
   pip install -r requirements.txt
   ```

2. **Migration Bajarish**: Loyihani database bilan ulash uchun quyidagi buyruqlarni ishga tushiring:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Superuser Yaratish**: Admin panelga kirish uchun superuser yarating:

   ```bash
   python manage.py createsuperuser
   ```

4. **Loyihani Ishga Tushirish**: Django serverni ishga tushiring:

   ```bash
   python manage.py runserver
   ```

# Authentication and Email Verification Views

Ushbu loyihada foydalanuvchilarni ro‘yxatdan o‘tkazish, elektron pochta orqali tasdiqlash, tizimga kirish va akkauntni faollashtirish jarayonlari qamrab olingan.

## 1. signup_view: Foydalanuvchini ro‘yxatdan o‘tkazish
**Funksional imkoniyatlari:**
- `UserRegistrationForm` yordamida foydalanuvchi ma’lumotlarini yig‘adi.
- Agar POST so‘rovi orqali yuborilgan ma’lumotlar `form.is_valid()` bo‘lsa:
  - Foydalanuvchi faolsiz (inactive) holatda saqlanadi.
  - Foydalanuvchining tasdiqlash tokeni yaratiladi.
  - Tasdiqlash havolasini o‘z ichiga olgan elektron pochta foydalanuvchiga yuboriladi (`send_email` yordamida).
  - Yuborilgandan so‘ng, foydalanuvchi `verify` sahifasiga yo‘naltiriladi.

**Shablonlar:**
- `registration/signup.html`: Ro‘yxatdan o‘tish shakli.

## 2. verify_email_view: Tasdiqlashni kutish sahifasi
Foydalanuvchiga elektron pochta tasdiqlash talab qilinayotganligini bildiradi.

**Shablon:**
- `registration/verify.html`.

## 3. confirm_email: Elektron pochta tasdiqlash
- Elektron pochta orqali yuborilgan UID va token orqali foydalanuvchi aniqlanadi.
- Agar token haqiqiy bo‘lsa:
  - Foydalanuvchi akkaunti faollashtiriladi.
  - Foydalanuvchi login sahifasiga yo‘naltiriladi.
- Agar token noto‘g‘ri yoki muddati tugagan bo‘lsa:
  - `signup` sahifasiga qayta yo‘naltiriladi.
  - Foydalanuvchiga xatolik xabari ko‘rsatiladi.

## 4. login_view: Tizimga kirish
**Funksional imkoniyatlari:**
- Foydalanuvchi `AuthenticationForm` orqali tizimga kirish uchun ma’lumot kiritadi.
- Agar kiritilgan ma’lumotlar to‘g‘ri bo‘lsa:
  - Foydalanuvchi autentifikatsiya qilinadi va tizimga kiradi.
  - Foydalanuvchi `home` sahifasiga yo‘naltiriladi.
- Agar ma’lumotlar noto‘g‘ri bo‘lsa:
  - Xatolik xabari ko‘rsatiladi.

**Shablonlar:**
- `registration/login.html`: Tizimga kirish shakli.

## Elektron pochta yuborish jarayoni
- Elektron pochta uchun tasdiqlash havolasi `registration/send_email.html` shablonidan yaratiladi.
- Bu tasdiqlash havolasi foydalanuvchining akkauntini faollashtirish imkonini beradi.

## Kodning asosiy ishlash tartibi
1. **Ro‘yxatdan o‘tish:** Foydalanuvchi o‘z ma’lumotlarini kiritadi va `signup_view` orqali tasdiqlash havolasini oladi.
2. **Tasdiqlash:** Foydalanuvchi elektron pochta orqali yuborilgan havolani bosib, akkauntini faollashtiradi (`confirm_email`).
3. **Tizimga kirish:** Faollashtirilgan foydalanuvchi tizimga kirib, `login_view` yordamida sayt xizmatlaridan foydalanadi.

## Izoh
- Elektron pochta funksiyasi uchun `.env` faylida maxfiy o‘zgaruvchilar sozlangan bo‘lishi kerak (`EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `SECRET_KEY` va hokazo).
- Batafsil ma’lumotni `.env.example` faylidan olishingiz mumkin.


## Muallif
Loyiha muallifi: [Javlonbek0205](https://github.com/Javlonbek0205)

**Loyiha bo'yicha qo'shimcha savollaringiz bo'lsa, GitHub orqali murojaat qiling!**
