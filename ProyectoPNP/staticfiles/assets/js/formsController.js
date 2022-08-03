
console.log("caraga correcta del controlador2")
const btnEliminacion = document.querySelectorAll(".btnEliminacion");

const data = document.querySelectorAll(".table-content");
let arrow = document.querySelectorAll(".arrow");
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");

(function(){

    for (var i = 0; i < arrow.length; i++) {
        arrow[i].addEventListener("click", (e)=>{
       let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
       arrowParent.classList.toggle("showMenu");
        });
      }
      sidebarBtn.addEventListener("click", ()=>{
        sidebar.classList.toggle("close");
      });

    console.log("llamando notificacion");
    //notificationSwall(document.title, "documentos listados con exito", "succes", "ok");

    
    /* Funtion to resize length of the data  */
    for (var i=0;i<data.length;i++) {
        if(!data[i].hasChildNodes()){
            continue;
        }      
        console.log(data[i].childNodes[0].nodeValue)
        //if (typeof data[i].children[0].nodeValue !== 'undefined'){
        var textValue = data[i].childNodes[0].nodeValue;
        if (textValue.length>20){
            data[i].childNodes[0].nodeValue = textValue.substr(0, 20)+"...";
        }else{
            data[i].childNodes[0].nodeValue = textValue;
        }
         
          
        
            
        
    }
    /* Function to show an alert to delets */

    btnEliminacion.forEach((btn)=>{
        console.log("se va a eliminar")
        btn.addEventListener("click", function(e){
            e.preventDefault();
            Swal.fire({
                title:"¿Confirma la eliminación del elemento?",
                text: "esta acción no se puede deshacer",
                showCancelButton:true,
                icon: "warning",
                confirmButtonText: "Sí, eliminar",
                cancelButtonText: "No, cancelar",
                confirmButtonColor: "#d33",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm:()=>{
                    
                    location.href = e.target.href
                },
                allowOutsideClick:()=>false,
                allowEscapeKey:()=>false,

            })
        })
    })
}
)();





