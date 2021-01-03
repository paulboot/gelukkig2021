$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				message : $('#messageInput').val(),
				sender : $('#senderInput').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
                $('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
                $('#submitButton').prop("disabled",true);
                $('#submitButton').html("<span class=\"spinner-border spinner-border-sm\" aria-hidden=\"true\"></span> Bezig...",true);
                $('#successAlert').hide();
				$('#errorAlert').hide();
                setTimeout(function()
                {
                    $('#successAlert').text('Verstuurde tekst: \"' + data.message + '\"').show();
                    $('#submitButton').html("Versturen",true);
                    $('#submitButton').prop("disabled",false);
                }, 1500);
			}
		});

		event.preventDefault();

	});

});
