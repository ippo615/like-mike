// START LAZYLINE 
 
var data;
var name;
var url;
var fullurl;
var dweet;

var pathObj = {
    "icons": {
        "strokepath": [
            {
                "path": "M220.225,443.314c0-0.79,0.631-1.494,1.494-1.494h7.227   c0.79,0,1.494,0.704,1.494,1.494v44.071h20.035c0.869,0,1.494,0.71,1.494,1.493v6.443c0,0.79-0.625,1.494-1.494,1.494h-28.756   c-0.862,0-1.494-0.704-1.494-1.494V443.314z",
                "duration": 300
            },
            {
                "path": "M259.864,443.314c0-0.79,0.71-1.494,1.494-1.494h7.306   c0.79,0,1.494,0.704,1.494,1.494v52.008c0,0.79-0.705,1.494-1.494,1.494h-7.306c-0.783,0-1.494-0.704-1.494-1.494V443.314z",
                "duration": 300
            },
            {
                "path": "M284.428,443.703c0-1.021,0.79-1.883,1.889-1.883h6.912   c1.025,0,1.889,0.861,1.889,1.883v21.213l19.798-22.312c0.315-0.395,0.783-0.783,1.493-0.783h7.859   c1.488,0,2.277,1.646,1.257,2.823l-20.509,23.103l21.996,26.32c0.79,1.02,0.158,2.75-1.408,2.75h-8.569   c-0.783,0-1.257-0.315-1.415-0.553l-20.502-25.293v23.957c0,1.027-0.863,1.889-1.889,1.889h-6.912   c-1.099,0-1.889-0.861-1.889-1.889V443.703z",
                "duration": 300
            },
            {
                "path": "M335.606,443.314c0-0.79,0.632-1.494,1.494-1.494h31.98   c0.862,0,1.488,0.704,1.488,1.494v6.437c0,0.79-0.626,1.494-1.488,1.494h-23.26v12.887h19.409c0.784,0,1.494,0.704,1.494,1.494   v6.522c0,0.862-0.71,1.488-1.494,1.488h-19.409v13.749h23.26c0.862,0,1.488,0.71,1.488,1.493v6.443c0,0.79-0.626,1.494-1.488,1.494   H337.1c-0.862,0-1.494-0.704-1.494-1.494V443.314z",
                "duration": 300
            },
            {
                "path": "M376.618,488.875l25.453-86.374c0.275-1.089,1.09-2.051,2.6-2.051h1.914c0.951,0,1.637,0.549,1.912,1.374   l18.585,61.922h0.275l37.186-61.922c0.549-0.825,1.234-1.374,2.324-1.374h2.049c0.963,0,1.914,0.962,1.914,2.051l1.236,91.867   c0,1.922-1.236,3.146-2.738,3.146h-13.123c-1.365,0-2.051-1.088-2.051-2.049l1.102-49.081c-0.141,0-0.275,0-0.416,0l-28.57,50.993   c-0.414,0.826-1.236,1.502-2.324,1.502h-2.188c-1.1,0-1.639-0.676-1.914-1.502l-13.946-50.993c0,0-0.139,0-0.275,0l-13.125,49.081   c-0.274,0.961-0.951,2.049-2.599,2.049h-12.985c-1.502,0-2.454-1.224-1.913-3.146 M374.999,495.368l1.619-5.493",
                "duration": 300
            },
            {
                "path": "M484.399,443.314c0.078-0.79,0.783-1.494,1.492-1.494h7.701c0.705,0,1.258,0.704,1.1,1.494l-7.312,52.008   c-0.072,0.79-0.783,1.494-1.488,1.494h-7.699c-0.711,0-1.258-0.704-1.1-1.494L484.399,443.314z",
                "duration": 300
            },
            {
                "path": "M508.653,443.703c0.158-1.021,0.941-1.883,1.963-1.883h7.385c0.947,0,1.572,0.861,1.414,1.883   l-2.982,21.213l18.463-21.682c0.863-1.025,1.572-1.414,3.219-1.414h7.779c1.336,0,1.811,1.414,0.789,2.593l-21.449,24.043   l15.869,25.926c0.553,1.021-0.236,2.435-1.574,2.435h-7.146c-1.494,0-2.119-0.315-2.83-1.572l-13.986-24.273l-3.377,23.957   c-0.078,1.027-1.02,1.889-1.883,1.889h-7.391c-1.02,0-1.566-0.861-1.488-1.889L508.653,443.703z",
                "duration": 300
            },
            {
                "path": "M556.849,443.314c0.08-0.79,0.785-1.494,1.494-1.494h29.072c0.783,0,1.258,0.704,1.178,1.494l-0.947,6.437   c-0.078,0.79-0.783,1.494-1.566,1.494h-20.113l-1.811,12.887h16.658c0.705,0,1.258,0.704,1.178,1.494l-0.941,6.522   c-0.158,0.862-0.867,1.488-1.572,1.488h-16.658l-1.961,13.749h20.191c0.783,0,1.178,0.71,1.1,1.493l-0.869,6.443   c-0.072,0.79-0.783,1.494-1.566,1.494h-29.07c-0.791,0-1.258-0.704-1.1-1.494L556.849,443.314z",
                "duration": 300
            },
            {
                "path": "M318.476,249.471c0.625-1.078,1.241-2.161,1.879-3.231    c0.475-0.794,0.992-1.562,1.464-2.358c0.124-0.208,0.219-0.477,0.209-0.713c-0.176-4.494-0.167-8.988,0.085-13.478    c0.133-2.377,0.399-4.748,0.608-7.122c0.01-0.114,0.055-0.225,0.097-0.389c0.708,0.092,1.397,0.181,2.124,0.275    c-0.707,5.916-0.918,11.815-0.794,17.868c0.186-0.234,0.302-0.367,0.404-0.511c3.472-4.891,7.32-9.467,11.493-13.772    c0.012-0.012,0.022-0.027,0.037-0.037c0.992-0.627,1.079-1.511,0.939-2.61c-0.534-4.205-0.738-8.437-0.703-12.675    c0.054-6.412,0.651-12.764,2.252-18.994c0.19-0.742,0.431-1.471,0.661-2.25c0.715,0.244,1.374,0.469,2.045,0.699    c-3.119,10.752-3.205,21.667-2.144,32.78c0.781-0.721,1.457-1.348,2.136-1.969c4.626-4.232,9.532-8.107,14.799-11.514    c0.558-0.361,0.767-0.726,0.71-1.401c-0.525-6.323,0.385-12.44,2.728-18.339c1.917-4.827,4.648-9.16,8.008-13.102    c4.963-5.823,10.854-10.557,17.312-14.61c8.788-5.515,18.185-9.696,28.083-12.768c0.13-0.041,0.264-0.068,0.435-0.112    c0.209,0.674,0.417,1.341,0.639,2.053c-0.168,0.061-0.319,0.124-0.475,0.172c-10.1,3.137-19.667,7.439-28.56,13.18    c-6.496,4.194-12.378,9.102-17.159,15.232c-3.909,5.013-6.732,10.561-8.088,16.807c-0.747,3.438-1.023,6.913-0.818,10.426    c0.01,0.168,0.033,0.334,0.056,0.561c0.189-0.106,0.337-0.182,0.479-0.27c9.778-6.038,20.234-10.513,31.313-13.54    c4.556-1.245,9.161-2.286,13.84-2.934c3.695-0.511,7.4-0.992,11.116-1.3c5.556-0.461,11.128-0.682,16.705-0.477    c3.066,0.113,6.138,0.199,9.192,0.468c3.306,0.291,6.602,0.723,9.888,1.197c5.101,0.735,10.114,1.893,15.052,3.372    c7.937,2.378,15.515,5.589,22.592,9.917c8.12,4.966,15.287,11.025,21.023,18.678c0.893,1.191,1.672,2.468,2.499,3.708    c0.131,0.197,0.237,0.412,0.381,0.662c-0.64,0.36-1.261,0.709-1.897,1.068c-0.569-0.875-1.108-1.745-1.687-2.588    c-3.493-5.091-7.775-9.442-12.547-13.33c-6.613-5.388-13.943-9.557-21.831-12.762c-5.7-2.315-11.554-4.159-17.591-5.346    c-3.891-0.765-7.811-1.418-11.743-1.922c-3.224-0.413-6.482-0.636-9.732-0.755c-3.94-0.145-7.889-0.179-11.83-0.097    c-3.356,0.071-6.717,0.275-10.058,0.603c-3.83,0.375-7.66,0.83-11.454,1.466c-7.13,1.197-14.092,3.075-20.889,5.555    c-7.779,2.837-15.171,6.463-22.186,10.863c-0.324,0.203-0.386,0.418-0.332,0.757c0.576,3.573,1.809,6.917,3.545,10.079    c2.618,4.771,6.107,8.851,10.046,12.566c5.882,5.55,12.492,10.111,19.43,14.219c8.374,4.957,17.122,9.163,26.071,12.971    c14.058,5.98,28.477,10.94,43.097,15.333c13.485,4.052,27.112,7.563,40.858,10.612c2.154,0.478,4.314,0.925,6.546,1.402    c-0.135,0.699-0.266,1.378-0.41,2.132c-0.851-0.17-1.668-0.325-2.48-0.499c-19.333-4.13-38.418-9.19-57.215-15.322    c-11.957-3.9-23.738-8.27-35.244-13.364c-8.344-3.694-16.49-7.774-24.278-12.541c-6.289-3.849-12.285-8.096-17.676-13.152    c-4.228-3.964-7.936-8.343-10.759-13.437c-1.517-2.737-2.855-6.356-3.637-10.133c-0.243,0.146-0.474,0.27-0.69,0.416    c-4.75,3.217-9.26,6.738-13.493,10.611c-1.063,0.973-2.11,1.963-3.138,2.972c-0.162,0.159-0.282,0.475-0.254,0.697    c0.525,4.271,1.336,8.492,2.318,12.68c2.449,10.457,6.016,20.531,10.438,30.306c5.574,12.32,12.138,24.09,19.978,35.113    c5.941,8.354,13.271,15.338,21.732,21.127c9.02,6.171,18.861,10.575,29.344,13.585c5.325,1.529,10.735,2.653,16.223,3.426    c6.211,0.875,12.448,1.286,18.719,1.169c1.197-0.022,2.395-0.092,3.659-0.142c0.059,0.698,0.116,1.389,0.181,2.155    c-0.74,0.048-1.449,0.12-2.159,0.136c-4.134,0.096-8.264,0.055-12.393-0.252c-5.681-0.423-11.309-1.21-16.878-2.398    c-12.192-2.6-23.706-6.945-34.333-13.516c-9.659-5.972-17.94-13.478-24.805-22.532c-3.943-5.202-7.324-10.771-10.626-16.389    c-5.672-9.647-10.602-19.66-14.639-30.1c-2.975-7.692-5.419-15.554-7.12-23.631c-0.6-2.846-1.051-5.722-1.572-8.584    c-0.027-0.15-0.072-0.298-0.128-0.529c-0.17,0.161-0.305,0.276-0.426,0.405c-4.602,4.892-8.886,10.04-12.548,15.684    c-0.145,0.223-0.22,0.541-0.208,0.809c0.505,11.153,2.301,22.104,5.108,32.901c3.105,11.948,7.042,23.623,11.419,35.156    c0.632,1.665,1.302,3.315,1.955,4.972c0.062,0.158,0.119,0.317,0.203,0.541c-0.68,0.269-1.338,0.529-2.039,0.806    c-0.726-1.849-1.446-3.643-2.135-5.449c-3.687-9.667-7.043-19.446-9.882-29.398c-1.799-6.307-3.411-12.663-4.526-19.128    c-0.651-3.779-1.112-7.592-1.601-11.397c-0.258-2.002-0.393-4.021-0.682-6.099c-0.557,0.994-1.113,1.988-1.686,3.011    c-0.666-0.335-1.32-0.663-1.973-0.991C318.476,249.54,318.476,249.505,318.476,249.471z",
                "duration": 300
            }
        ],
        "dimensions": {
            "width": 800,
            "height": 800
        }
    }

}; 
 
   // END LAZYLINE
 
// CALL LAZYLINE FUNCTION
$(document).ready(function() {    
        $.ajax(); 
        $('#icons').lazylinepainter( 
 {
    "svgData": pathObj,
    "strokeWidth": 3,
    "strokeColor": "white"
}).lazylinepainter('paint'); 

      }); // END LAZYLINE FUNCTION

$(document).ajaxStart(function(){
    $("#aboutme").hide();
    $("#showData").hide();
     $("#restart").hide();
}); // HIDE ABOUT ME TO START


$("#postintro").click(function(){
     $("#intro").hide();
      $("#icons").hide();
    $("#aboutme").show();
    data = $('form').serialize();
     url = $('input').val();
     fullurl="http://www.dweet.io/follow/"+url;
     //window.open(fullurl);


   /* $("#showData").show();

   dweetio.listen_for(url, function(dweet){
    console.info("DWEETING!!");
    });
*/

     
}); 

/*function showData(){
     dweetio.get_latest_dweet_for(url, function(err, dweet){

     dweet = dweet[0]; // Dweet is always an array of 1

    var name = dweet.thing; // The generated name
    console.log(dweet.content); // The content of the dweet
    console.log(dweet.created); // The create date of the dweet

});

}*/

/*
function showData(){
dweetio.listen_for(url+"-score", function(dweet){
    
   // var dweet = dweet[0]; // Dweet is always an array of 1
    console.log(dweet.thing); // The generated name
    console.log(dweet.content); // The content of the dweet
    console.log(dweet.created); // The create date of the dweet
    $('#showData').html("hello" + dweet.content);


});
} */

function collectData(){
dweetio.listen_for(url, function(dweet){
    
   // var dweet = dweet[0]; // Dweet is always an array of 1
    console.log(dweet.thing); // The generated name
    console.log(dweet.content); // The content of the dweet
    console.log(dweet.created); // The create date of the dweet
    $('#showData').html("hello" + dweet.content);
    

 
});
}



$("#postintro").click(function(){
        setTimeout(function(){$('#aboutme').html("READY?")},000);

        setTimeout(function(){$('#aboutme').html(3)},1000);
         setTimeout(function(){$('#aboutme').html(2)},2000);
        setTimeout(function(){$('#aboutme').html(1)},3000);
        setTimeout(function(){$('#aboutme').html("SHOOT!")},4000);
        setTimeout(function(){ dweetio.dweet_for("si-hacks-2015-05-16-blah-start", {thing:url}, function(err, dweet){

            console.log(dweet.thing); // "my-thing"
            console.log(dweet.content); // The content of the dweet
            console.log(dweet.created); // The create date of the dweet
     });




        },4000);

        setTimeout(function(){$('#score').html("YOU'RE LIKE MIKE!")},6000);
          
         setTimeout(function() {$("#restart").show()},6000);


    
       /* setTimeout(function(){
            collectData();
    }, 7000);
         setTimeout(function(){
            dweetio.stop_listening_for(url);
    }, 9000);*/



        







       /* function makeUpdateCountdown(n){
            return function(){
               $("#aboutme").html(n); 
            }
        }

        for (n = 3; n > 0; n-=1) { 
           setTimeout(makeUpdateCountdown(n), (3-n)//*1000);
        }

        var n = 3;
        setTimeout(function blah(){
            $('#aboutme').html(n);
            if( n == 0 ){ return }
            n -= 1;
            setTimeout(blah,1000);
        },1000);

        if(n == 0){
            $("#aboutme").html("SHOOT!"); 
        }
*/

    $("#countdown").html("RESTART"); 

}); 


$("#restart").click(function(){

        $('#score').html("")
        setTimeout(function(){$('#aboutme').html("READY?")},000);

        setTimeout(function(){$('#aboutme').html(3)},1000);
         setTimeout(function(){$('#aboutme').html(2)},2000);
        setTimeout(function(){$('#aboutme').html(1)},3000);
        setTimeout(function(){$('#aboutme').html("SHOOT!")},4000);
        setTimeout(function(){ dweetio.dweet_for("si-hacks-2015-05-16-blah-start", {thing:url}, function(err, dweet){

            console.log(dweet.thing); // "my-thing"
            console.log(dweet.content); // The content of the dweet
            console.log(dweet.created); // The create date of the dweet
     });




        },4000);

        setTimeout(function(){$('#score').html("YOU'RE LIKE MIKE!")},6000);
          


    
       /* setTimeout(function(){
            collectData();
    }, 7000);
         setTimeout(function(){
            dweetio.stop_listening_for(url);
    }, 9000);*/



        







       /* function makeUpdateCountdown(n){
            return function(){
               $("#aboutme").html(n); 
            }
        }

        for (n = 3; n > 0; n-=1) { 
           setTimeout(makeUpdateCountdown(n), (3-n)//*1000);
        }

        var n = 3;
        setTimeout(function blah(){
            $('#aboutme').html(n);
            if( n == 0 ){ return }
            n -= 1;
            setTimeout(blah,1000);
        },1000);

        if(n == 0){
            $("#aboutme").html("SHOOT!"); 
        }
*/

    $("#countdown").html("RESTART"); 

}); 


console.log(dweet);
// CALL COUNTDOWN


    /* TEST TO LOAD IN DATA
    $.get( "https://dweet.io:443/get/latest/dweet/for/tight-respect", function( data ) {
    $( "#aboutme" ).html( data );
    alert( "Load was performed." + data ); }); */



