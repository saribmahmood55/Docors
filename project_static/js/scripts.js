$(function () {
			var favtImg = $('#favt');
			console.log("Hello");
			favtImg.submit(function (ev) {
				$.ajax({
				type:"POST",
				url: "{% url 'practitioner' practitioner.slug %}",
				data: {
					favt: "favourite",
					csrfmiddlewaretoken: '{{ csrf_token }}',
				},
				dataType : 'json'
			});
			ev.preventDefault();
		});
	});
$(function () {
			var favtImg = $('#favt');
			console.log("Hello");
			favtImg.submit(function (ev) {
				$.ajax({
				type:"POST",
				url: "{% url 'practitioner' practitioner.slug %}",
				data: {
					favt: "favourite",
					csrfmiddlewaretoken: '{{ csrf_token }}',
				},
				dataType : 'json'
			});
			ev.preventDefault();
		});
	});
$(function () {
			var favtImg = $('#favt');
			console.log("Hello");
			favtImg.submit(function (ev) {
				$.ajax({
				type:"POST",
				url: "{% url 'practitioner' practitioner.slug %}",
				data: {
					favt: "favourite",
					csrfmiddlewaretoken: '{{ csrf_token }}',
				},
				dataType : 'json'
			});
			ev.preventDefault();
		});
	});