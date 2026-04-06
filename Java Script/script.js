function check() {
    let input = document.getElementById("pass").value;
    let output = document.getElementById("out");

    if (input === "first_key") {

        let md5_hash = "c9f0f895fb98ab9159f51fd0297e236d";
        let sha_hash = "6e6bc4e49dd477ebc98ef4046c067b9f9a4d5a2f03f06abbdece274164a49158";

        output.innerHTML =
            "✅ Correct!<br><br>" +
            "MD5: " + md5_hash + "<br>" +
            "SHA256: " + sha_hash;

    } else {
        output.innerHTML = "❌ Wrong key";
    }
}