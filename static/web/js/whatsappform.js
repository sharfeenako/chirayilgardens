
// JavaScript code to handle form submission and open WhatsApp chat
document.getElementById("inquiryForm").onsubmit = function (event) {
    event.preventDefault(); // Prevent form submission

    // Get form data
    const formData = new FormData(event.target);
    const name = formData.get("name");
    const quantity = formData.get("quantity");
    const phoneno = formData.get("phoneno");
    const package = formData.get("package");
    const comment = formData.get("comment");
    const product = formData.get("product");
    
    const fertilizerSelect = document.querySelector('select[name="fertilizer_package"]');
    var fertilizer_package = fertilizerSelect.options[fertilizerSelect.selectedIndex].innerHTML;
    if (fertilizer_package == 'Select Fertilizer'){
        fertilizer_package = 'Not Needed'
    }
    const medicineSelect = document.querySelector('select[name="medicine_package"]');
    var medicine_package = medicineSelect.options[medicineSelect.selectedIndex].innerHTML;

    if (medicine_package == 'Select Medicine'){
        medicine_package = 'Not Needed'
    }
    // Define your WhatsApp number (include country code)
    const whatsappNumber = "8589993015";


    // Create the WhatsApp message
    const whatsappMessage = `Name: ${name}\nQuantity: ${quantity}\nProduct: ${product}\nPhone no:${phoneno}\nPackage:${package}\nFertilizer:${fertilizer_package}\nMedicine:${medicine_package}\nComment: ${comment}`;

    // Encode the message for use in the URL
    const encodedMessage = encodeURIComponent(whatsappMessage);

    // Create the WhatsApp link
    const whatsappURL = `https://api.whatsapp.com/send?phone=${whatsappNumber}&text=${encodedMessage}`;

    // Open the WhatsApp chat in a new tab
    window.open(whatsappURL, "_blank");
};
