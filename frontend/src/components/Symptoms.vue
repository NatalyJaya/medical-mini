<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const symptoms = ref([]);

const newSymptom = ref({
  date: "",
  symptom: "",
  severity: 1,
  notes: ""
});

const loadSymptoms = async () => {
  const response = await api.get("/symptoms");
  symptoms.value = response.data;
};

const createSymptom = async () => {
  await api.post("/symptoms", newSymptom.value);
  await loadSymptoms();

  newSymptom.value = {
    date: "",
    symptom: "",
    severity: 1,
    notes: ""
  };
};

onMounted(loadSymptoms);
</script>

<template>
  <h2>Symptoms</h2>

  <h3>Add Symptom</h3>

  <input type="date" v-model="newSymptom.date" />
  <input placeholder="Symptom" v-model="newSymptom.symptom" />
  <input type="number" min="1" max="5" v-model="newSymptom.severity" />
  <input placeholder="Notes" v-model="newSymptom.notes" />

  <button @click="createSymptom">Add</button>

  <h3>History</h3>
  <ul>
    <li v-for="s in symptoms" :key="s.id">
      {{ s.date }} - {{ s.symptom }} ({{ s.severity }})
    </li>
  </ul>
</template>
