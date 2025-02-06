document.addEventListener("DOMContentLoaded", function() {
    const mcqForm = document.getElementById("mcqForm");
    const processorOptions = document.getElementById("processor-options");
    const gpuOptions = document.getElementById("gpu-options");
    const displayOptions = document.getElementById("display-options");
    const osOptions = document.getElementById("os-options");
    const heavyos = document.getElementById("heavy-options");
    const touchoptions=document.getElementById("touch-options");
    const expandablememory=document.getElementById("expandable-memory");
    const priceoptions=document.getElementById("price");
    
    const gamerRadioButton = document.querySelector('input[name="q1"][value="Gamer"]');
    const studentRadioButton = document.querySelector('input[name="q1"][value="Student"]');
    const businessRadioButton = document.querySelector('input[name="q1"][value="Business"]');
    // const macRadioButton = document.querySelector('input[name="os"][value="Mac"]');
    function toggleOptions(displayProcessor, displayGPU, displayDisplay, displayOS,d1,d2,d3,d4) {
        processorOptions.style.display = displayProcessor ? "block" : "none";
        heavyos.style.display = d1 ? "block" : "none";
        gpuOptions.style.display = displayGPU ? "block" : "none";
        displayOptions.style.display = displayDisplay ? "block" : "none";
        osOptions.style.display = displayOS ? "block" : "none";
        touchoptions.style.display=d2 ? "block" : "none";
        expandablememory.style.display=d3 ? "block" : "none";
        priceoptions.style.display=d4 ? "block" : "none";

    }

    let primary_profile;
    let secondary_profile;
    let processor;
    let graphics;
    let resolution;
    let os;
    let touch;
    let memory;
    let price;


    mcqForm.addEventListener("change", function(event) {
        if (event.target.name === "q1" && event.target.type === "radio" && event.target.checked) {
            const selectedOption = event.target.value;

            primary_profile = selectedOption;

            if (selectedOption == 0) {
                toggleOptions(true, true, true, false,true,true,true,true);
            } else if (selectedOption == 1) {
                toggleOptions(false, false, true, true,true,true,true,true);
            } else if (selectedOption == 2) {
                toggleOptions(true, false, true, true,false,true,false,true);
            } else {
                toggleOptions(false, false, false, false,false,false,false,false);
            }
        }
    });

    // mcqForm.addEventListener("submit", function(event) {
    //     event.preventDefault();
    //     // Handle form submission here if needed
    // });


    mcqForm.addEventListener("submit", function (event) {
        event.preventDefault();

        // var allChecked = true;
        var r1 = document.getElementsByName("display");
        var selected = false;
        for (var i = 0; i < r1.length; i++) {
            if (r1[i].checked) {
                selected = true;
                resolution = r1[i].getAttribute('value');
                break;
            }
            else
            selected = false;
        }

        // var r2 = document.getElementsByName("q1");
        // var selected = false;
        // for (var i = 0; i < r2.length; i++) {
        //     if (r2[i].checked) {
        //         selected = true;
        //         break;
        //     }
        //     else
        //     selected = false;
        // }
        
        var r3 = document.getElementsByName("os_");
        var selected = false;
        for (var i = 0; i < r3.length; i++) {
            if (r3[i].checked) {
                selected = true;
                secondary_profile = r3[i].getAttribute('value');
                break;
            }
            else
            selected = false;
        }

        var r4 = document.getElementsByName("processor");
        var selected = false;
        for (var i = 0; i < r4.length; i++) {
            if (r4[i].checked) {
                selected = true;
                processor = r4[i].getAttribute('value')
                break;
            }
            else
            selected = false;
        }

        var r5 = document.getElementsByName("gpu");
        var selected = false;
        for (var i = 0; i < r5.length; i++) {
            if (r5[i].checked) {
                selected = true;
                graphics = r5[i].getAttribute('value')
                break;
            }
            else
            selected = false;
        }
        
        var r6 = document.getElementsByName("os");
        var selected = false;
        for (var i = 0; i < r6.length; i++) {
            if (r6[i].checked) {
                selected = true;
                os = r6[i].getAttribute('value');
                break;
            }
            else
            selected = false;
        }
        var r9 = document.getElementsByName("expandable-memory");
        var selected = false;
        for (var i = 0; i < r9.length; i++) {
            if (r9[i].checked) {
                selected = true;
                memory = r9[i].getAttribute('value')
                break;
            }
            else
            selected = false;
        }
        var r8 = document.getElementsByName("touch");
        var selected = false;
        for (var i = 0; i < r8.length; i++) {
            if (r8[i].checked) {
                selected = true;
                touch = r8[i].getAttribute('value')
                break;
            }
            else
            selected = false;
        }
        var r7 = document.getElementsByName("price");
        var selected = false;
        for (var i = 0; i < r7.length; i++) {
            if (r7[i].checked) {
                selected = true;
                price = r7[i].getAttribute('value')
                break;
            }
            else
            selected = false;
        }
        if (selected) {
            // window.location.href = "https://www.google.com";
// User Primary Profile 0 : Gamer, 1 : Student, 2 : Business
// User secondary Profile 0 : casual, 1 : Lightweight, 2 : Heavy 
// Price 0 : below 50k, 1 : 50k-100k, 2 : 100k - 150k, 3 : 150k - 200k, 4 : 200k+
// OS 0 : macos, 1 : windows 
// resolution  0 : 1080p, 1 : 1440p, 2 : 2160p
// graphics card 0 : NVIDIA, 1 : AMD
// Processor 0 : AMD, 1  : INTEL

            user_specs = {
                "primary_profile" : primary_profile,
                "secondary_profile" : secondary_profile,
                "processor" : processor,
                "graphics" : graphics,
                "resolution" : resolution,
                "os" : os,
                "expandable_memory" : memory,
                "price" : price,
                "touch" : touch
            }
            // console.log(user_specs)

            let data_options = {
                method : 'POST',
                body : JSON.stringify(user_specs),
                headers : {
                    'Content-Type' : 'application/json'
                }
            };

            fetch('link',data_options)
                .then(function(response){
                    if(!response.ok){
                        throw new Error("Network response was not ok");
                    }
                    return response.json()
                })
                .then(function(data){
                    console.log(data);
                })
                .catch(function(error){
                    console.log(error);
                })
            

        } else {
            alert("Please select options for all questions");
        }
    });
});