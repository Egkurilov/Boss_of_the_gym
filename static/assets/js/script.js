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
$(document).on('click', ".exersise-to-user", function (e) {
    $this = $(this)
    e.preventDefault()
    $('#DialogBasic').modal('show').find(`input[name="ex-id"]`).val($(this).data('exersise-id'));
    $('#DialogBasic').find(".modal-body").text(`Вы хотите добавить упражнение "${$this.text()}" в свой список упражнений?`)
}).on('submit', '#useradd-ex-form', function (e) {
    e.preventDefault()
    $.post("task/add", $("#useradd-ex-form").serialize(), function (response, textStatus, jqXHR) {
        if (response.success === false) {
            return _noty(response.message, 'error');
        }
        $this.parents('.task-item').slideUp("fast", function () {
            $(this).remove()
        })
        return _noty(response.message, 'success');
    }, "json");
})
