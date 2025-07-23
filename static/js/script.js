document.addEventListener("DOMContentLoaded", () => {
    const passengerCountInput = document.getElementById("passenger_count");
    const passengerDetailsDiv = document.getElementById("passengerDetails");

    if (passengerCountInput) {
        passengerCountInput.addEventListener("input", () => {
            const count = parseInt(passengerCountInput.value) || 0;
            passengerDetailsDiv.innerHTML = "";
            for (let i = 1; i <= count; i++) {
                passengerDetailsDiv.innerHTML += `
                    <div class="row mb-2">
                        <div class="col-md-4">
                            <label class="form-label">Passenger ${i} Name</label>
                            <input type="text" name="passenger_name_${i}" class="form-control" required>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label">Age</label>
                            <input type="number" name="passenger_age_${i}" class="form-control" required>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label">Gender</label>
                            <select name="passenger_gender_${i}" class="form-select" required>
                                <option value="">Select</option>
                                <option value="Male">Male</option>
                                <option value="Female">Female</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>
                    </div>`;
            }
        });
    }
});
