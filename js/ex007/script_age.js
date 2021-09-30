function verification() {
    var year = new Date();
    var nowyear = year.getFullYear();
    var formyear = document.querySelector('input#year');
    var formresponse = document.querySelector('div#response');

    if (Number(formyear.value.length) <= 3 || Number(formyear.value) > nowyear) {
        window.alert("[ERROR] verify the field and try again");
    }
    else {
        var formgender = document.getElementsByName('radgen');
        var age = nowyear - Number(formyear.value);
        var gender = '';
        var img = document.createElement('img');
        img.setAttribute('id', 'photo')

        if (formgender[0].checked) {
            gender = 'male';

            if (age >= 0 && age < 12) {
                //children
                img.setAttribute('src', 'pictures/profile/children_male.png')
            }

            else if (age < 22) {
                //young
                img.setAttribute('src', 'pictures/profile/young_male.png')
            }

            else if (age < 60) {
                //adult
                img.setAttribute('src', 'pictures/profile/adult_male.png')
            }

            else {
                //old
                img.setAttribute('src', 'pictures/profile/old_male.png')
            }

        }
        else if (formgender[1].checked) {
            gender = 'female'

            if (age >= 0 && age < 12) {
                //children
                img.setAttribute('src', 'pictures/profile/children_female.png')
            }

            else if (age < 22) {
                //young
                img.setAttribute('src', 'pictures/profile/young_female.png')
            }

            else if (age < 60) {
                //adult
                img.setAttribute('src', 'pictures/profile/adult_female.png')
            }

            else {
                //old
                img.setAttribute('src', 'pictures/profile/old_female.png')
            }
        }

        formresponse.innerHTML = `detect ${gender} with ${age} years old`;
        formresponse.appendChild(img);
    }
}
