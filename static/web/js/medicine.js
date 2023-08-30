
// JavaScript code to handle form submission and open WhatsApp chat
document.getElementById("inquiryForm2").onsubmit = function (event) {
    event.preventDefault(); // Prevent form submission

    // Get form data
    const formData = new FormData(event.target);
    const name = formData.get("name");
    const phoneno = formData.get("phoneno");
    const package = formData.get("package");
    const comment = formData.get("comment");
    const product = formData.get("product");


    // Define your WhatsApp number (include country code)
    const whatsappNumber = "8589993015";

    // Get the product name directly from the input field (placeholder attribute)

    // Create the WhatsApp message
    const whatsappMessage = `Name: ${name}\nMedicine: ${product}\nPhone no:${phoneno}\nPackage:${package}\nComment: ${comment}`;

    // Encode the message for use in the URL
    const encodedMessage = encodeURIComponent(whatsappMessage);

    // Create the WhatsApp link
    const whatsappURL = `https://api.whatsapp.com/send?phone=${whatsappNumber}&text=${encodedMessage}`;

    // Open the WhatsApp chat in a new tab
    window.open(whatsappURL, "_blank");
};
