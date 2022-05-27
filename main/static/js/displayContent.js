var mall_id_global = ""

var select_ = function() {
  $.ajax({
            type: 'GET',
            url: "{% url 'shops_list' %}",
	  		dataType: 'json',
            success: function (response) {
				$("#sh_item").html(response)
            },
            error: function (response) {
                console.log(response)
            }
        })
};

function displayShops(){

	 document.getElementById('im').style.display = "none";
	 document.getElementById('sttt').style.display = "none";

	 document.getElementById('hm').style.display = "none";
	 document.getElementById('bl').style.display = "none";

	 document.getElementById('sh').style.display = "block";
    }

function displayMalls(){

	 document.getElementById('im').style.display = "block";
	 document.getElementById('sttt').style.display = "table";
	 document.getElementById('hm').style.display = "block";
	 document.getElementById('bl').style.display = "block";
	 document.getElementById('sh').style.display = "none";
    }

function displayProducts(){
	document.getElementById('sh').style.display = "none";
}


function displayContent(o) {
    var result = ""
	object = o
	result+="</br></br>"
	result = (result + "<div style='width: 400px;' >" +
		"<a class='btn btn-outline-success' style='width: 50%;' href='#' onclick='displayMalls()'>Info</a>" +

		"<a class='btn btn-outline-success' style='width: 50%;' href='#' onclick='displayShops()'>Shops</a>" + "</div>")


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

		if (Object.keys(o)[key] == 'shops'){
			result += "<div id='sh' style='display: none;'>"



			for (var keyy in o.shops){

				   result = (result +
					   "<hr><div id='sh_item' style='border: solid 2px #BBB1BD; border-radius: 8px; width: 400px; height: 125px; margin: 0; align-content: center;'><div id='sh_im' style=' width: 150px; height: 120px; float: left;" +
					   "'><a href='#' onclick='displayProducts()'><img style='float: left; width: 100%; height: 100%;' src = "  + o.shops[keyy].shop_image +  "></a></div>"
					   + "<div id='sh_name' style=' width: 60%; height: 20%;  float: left;'>" + "<a href='#' style='float: left; margin: 2px; font-size: 20px;'>" + o.shops[keyy].shop_name + "</a>" + "</br>"+ "</div>"
					   + "<div id='sh_info' style='width: 60%; height: 120px; float: left'><p style='  margin: 5px; width: 100%; height: 100%; opacity:1;'>" + "</br>" + o.shops[keyy].info + "</p></div></div>"
				   )
			}
			result += "</div>"
		}


	}

	for (var key in Object.keys(o)) {

		if (Object.keys(o)[key] == 'image_link'){
			   result = (result + "<div id='im'><img style='width: 100%; height: 200px;' src = " + Object.values(o)[key] + "></div>" )
			   result = result + "</br></br></br>"
			}


	}
	result = result + "<div id='stt'>"
	for (var key in Object.keys(o)) {

		if (Object.keys(o)[key] == 'addr_street'){
   			result = (result
			+ "<table class='table-hover table' id='sttt'>"
		  + "<tbody>"
          + "<tr><th>"
          + "<h6 >Address street: </h6>"
          + "</th><th>"
          + "<h6 style='text-align: right;'>" + Object.values(o)[key] + "</h6>"
          + "</th></tr>" + "</tbody>" + "</table>")      }

	}
	result+="</div>"

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