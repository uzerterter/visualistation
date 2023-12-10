import { writable } from 'svelte/store';

// Creating a writable store for 'selectedYear'
export const selectedYear = writable(2017); // Initial year is set to 2017
