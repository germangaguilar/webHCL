const oForm=document.forms.resform;
const oDate=oForm.DateIn;
const oBttn=oForm.querySelector('[type="submit"]');


oBttn.addEventListener('click',e=>{
  if( oDate.value!='' ){
    const date=new Date( oDate.value );
    const opts={ year:'numeric', month:'2-digit', day:'2-digit' };
    const formatted=new Intl.DateTimeFormat( 'en-US', opts ).format( date );

    console.info( 'Formatted date value: %s',formatted )
 }
});
