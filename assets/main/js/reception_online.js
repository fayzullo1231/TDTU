document.getElementById('yoshingiz').addEventListener('input', function () {
    // Faqat raqamlarni qabul qiladi (harflarni bloklaydi)
    this.value = this.value.replace(/[^0-9]/g, '');

    // Agar qiymat bo‘sh bo‘lsa, chiqib ketadi
    if (this.value === "") return;

    // Agar birinchi raqam 0 bo‘lsa, uni 1 ga almashtiradi
    if (this.value.length === 1 && this.value === "0") {
        this.value = "1";
    }

    // Agar birinchi raqam 4 dan katta bo‘lsa, avtomatik 4 qilib qo‘yadi
    if (this.value.length === 1 && parseInt(this.value, 10) > 4) {
        this.value = "4";
    }

    // Agar qiymat 40 dan katta bo‘lsa, avtomatik 40 qilib qo‘yadi
    if (parseInt(this.value, 10) > 40) {
        this.value = 40;
    }

    // Ortacha nollarni olib tashlaydi (masalan, 00012 -> 12)
    this.value = this.value.replace(/^0+(?=\d)/, '');
});

document.getElementById('yoshingiz').addEventListener('keydown', function (event) {
    // Foydalanuvchi birinchi raqam sifatida 0 yoki 4 dan kattasini kiritolmasin
    if (this.value.length === 0 && (event.key === "0" || event.key > "4")) {
        event.preventDefault();
    }
});


function formatPhoneNumber(event) {
    let input = event.target;
    let value = input.value;

    // Faqat raqamlarni olish (boshqa belgilarni olib tashlash)
    value = value.replace(/\D/g, '');

    // Agar value hali ham +998 bo'lsa, qiymatni o'zgartirmaymiz
    if (value.length <= 3) {
        value = '+998'; // Faqat +998 qoladi
    } else if (value.length <= 5) {
        value = '+998 ' + value.substring(3, 5); // 2 ta raqamdan keyin bo'sh joy
    } else if (value.length <= 8) {
        value = '+998 ' + value.substring(3, 5) + ' ' + value.substring(5, 8); // 3 ta raqamdan keyin bo'sh joy
    } else if (value.length <= 10) {
        value = '+998 ' + value.substring(3, 5) + ' ' + value.substring(5, 8) + ' ' + value.substring(8, 10); // 4 ta raqamdan keyin bo'sh joy
    } else if (value.length <= 12) {
        value = '+998 ' + value.substring(3, 5) + ' ' + value.substring(5, 8) + ' ' + value.substring(8, 10) + ' ' + value.substring(10, 12); // 5 ta raqamdan keyin bo'sh joy
    } else if (value.length <= 14) {
        value = '+998 ' + value.substring(3, 5) + ' ' + value.substring(5, 8) + ' ' + value.substring(8, 10) + ' ' + value.substring(10, 12) + ' ' + value.substring(12, 14); // 6 ta raqamdan keyin bo'sh joy
    }

    // Inputga formatlangan qiymatni o'rnatish
    input.value = value;
}

