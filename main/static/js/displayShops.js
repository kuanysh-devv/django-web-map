
function displayShops(o) {
    var result = ""
	result = (result + "<div style='display: inline-block'>" + "<a href=''>Info</a>" + "</div>")
    var data = Places.objects.all()
	for (var key in Object.keys(o)) {

		if (Object.keys(o)[key] == 'name'){
			result = (result + "<div style='display: flex; flex-flow: column'> </br><div id='na'><h2 style='text-underline-position: auto'>" + Object.values(o)[key] + "</h2></div>")
		}

		for (var key in Object.keys(o)) {
			if (Object.keys(o)[key] == 'id') {

				mall_id_global = Object.values(o)[key]
			}
		}




	}
	for (var key in Object.keys(o)) {

		if (Object.keys(o)[key] == 'image_link'){
			   result = (result + "<div id='im'><img style='width: 100%; height: 200px;' src = " + Object.values(o)[key] + "></div>" )
			   result = result + "</br></br></br>"
			}


	}
	for (var key in Object.keys(o)) {

		if (Object.keys(o)[key] == 'addr_street'){
   			result = (result
                + "<div id='st'><table class='table table-hover' style='order: 3'>"
          + "<tr><th>"
          + "<h6>Address street: </h6>"
          + "</th><th>"
          + "<h6 style='text-align: right;'>" + Object.values(o)[key] + "</h6>"
          + "</th></tr>" + "</table></div>")      }


	}
	for (var key in Object.keys(o)) {

		if (Object.keys(o)[key] == 'addr_housenumber'){
			result = (result
			+ "<div id='hm'><table class='table table-hover'>"
          + "<tr><th>"
          + "<h6 >Address housenumber: </h6>"
          + "</th><th>"
          + "<h6 style='text-align: right;'>" + Object.values(o)[key] + "</h6>"
          + "</th></tr>" + "</table></div>")      }


	}
	for (var key in Object.keys(o)) {

		if (Object.keys(o)[key] == 'building_levels'){
   		result = (result
        + "<div id='bl'><table class='table table-hover'>"
          + "<tr><th>"
          + "<h6>Building levels: </h6>"
          + "</th><th>"
          + "<h6 style='text-align: right;'>" + Object.values(o)[key] + "</h6>"
          + "</th></tr>" + "</table></div>" + "</div>")       }


	}

	return result
}