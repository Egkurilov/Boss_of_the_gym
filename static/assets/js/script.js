$(document).ready(function () {
    $("#settings-form").ajaxForm({
        url: '/user/settings',
        type: 'post',
        success: function(data, status, xhr, form) {
            console.log(data);
            if (data.result == 'error') {
                return _noty('error', data.message)
            }
            return _noty('success', 'Успех!')
        }
    });
    $("#login").ajaxForm({
        url: '/public/auth/login',
        type: 'post',
        success: function(data, status, xhr, form) {
            console.log(data);
            if (data.result == 'error') {
                return _noty('error', data.message)
            }
            return _noty('success', 'Авторизация прошла успешно')
        }
    });
});

const _noty = (type, message, time = 3000) => {
    if(type == 'error') {
        $("#toast-error .text").html(message)
        toastbox('toast-error', time)
    } else {
        $("#toast-success .text").html(message)
        toastbox('toast-success', time)
    }
    
}