
// FIELDS VALIDATIONS
function validateEmail(email){
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validateAll(){
    var name = $("#name").val();
    var phone = $("#phone").val();
    var email = $("#email").val();
    var age = $("#age").val();
    var gender = $("#gender").val();

    if (name==''){
        swal("Opss !", "Name field can not be empty", "error")
        return false;
    }
    else if (phone ==''){
        swal("Opss !", "Phone field can not be empty", "error")
        return false;
    }
    else if (email ==''){
        swal("Opss !", "Email field can not be empty", "error")
        return false;
    }
    else if (!(validateEmail(email))){
        swal("Opss !", "Put a valid email address", "error")
        return false;
    }
    else if (age ==''){
        swal("Opss !", "Age field can not be empty", "error")
        return false;
    }
    else if (age > 120){
        swal("Denied !", "The maximum value is 120 years", "error")
        $("#age").val("");
        return false;
    }
    else if (gender ==''){
        swal("Opss !", "Please select gender", "error")
        return false;
    }
    else{
        return true;
    }
}
$("#btn-add").bind("click", validateAll)


// allow only letter
$(document).ready(function(){
    jQuery('input[name="name').keyup(function(){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');
        jQuery(this).val(allow);
    });

    // prevent starting with space
    $("input").on("keypress", function(e){
        if (e.which == 32 && ! this.value.length)
        e.preventDefault();
    });
});


// SCRIPT TO PUT FIRST LETTER CAPTALIZED
$("#name").keyup(function() {
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){ return $1.toUpperCase( ); }));
});

// SCRIPT TO LOWERCASE input email
$(document).ready(function() {
    $('#email').keyup(function(){
        this.value = this.value.toLowerCase();
    });
});

// SCRIPT TO MAKE AGE ACCEPT ONLY NUMBER
$('#age').keyup(function(){
    if(!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9.]/).join('');
    }
})

// Phone mask 
$(document).ready(function() {
    $("#phone").inputmask("(234) 999-999-9999", { "onincomplete": function() {
        swal("Opsss !", "Incomplete phone number", "error");
        return false;
        } 
    });
});