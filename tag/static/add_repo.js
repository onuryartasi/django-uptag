
var add_repo = document.getElementById('add_repo');

var i=0
add_repo.addEventListener('click', function() {
    var repo={{ form }};
    $("#create_form").append(repo);
    var dell_repo = document.getElementById('del_repo');
    i=i+1;
      }, false);

    function test(id){
      var res=id.substring(9,);
      var element = document.getElementById("repo_form_"+res);
      element.parentNode.removeChild(element);
    }
