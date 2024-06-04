import gradio as gr

# Selection Sort algorithm
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Sorting function to be called by Gradio
def sort_array(array, algorithm):
    # Convert input string to a list of integers
    array = list(map(int, array.split(',')))
    
    # Select the appropriate sorting algorithm
    if algorithm == "Selection Sort":
        sorted_array = selection_sort(array)
    elif algorithm == "Insertion Sort":
        sorted_array = insertion_sort(array)
    
    return sorted_array

# Gradio interface
with gr.Blocks() as demo:
    # Add CSS for custom styling
    gr.HTML("""
    <style>
    body {background-color: #f0f8ff;}
    h1 {color: blue;}
    h3 {color: green;}
    .gr-button {color: white; background-color: blue;}
    </style>
    """)
    
    gr.Markdown("<h1>Array Sorting UI</h1>")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("<h3>Input Section</h3>")
            # Input field for array
            array_input = gr.Textbox(
                label="Enter array (comma-separated)",
                placeholder="e.g., 3,1,4,1,5,9,2,6,5"
            )
            # Radio buttons for algorithm selection
            algorithm_choice = gr.Radio(
                ["Selection Sort", "Insertion Sort"],
                label="Select sorting algorithm"
            )
            # Button to trigger sorting
            sort_button = gr.Button("Sort Array")
        
        with gr.Column():
            gr.Markdown("<h3>Output Section</h3>")
            # Textbox to display sorted array
            result = gr.Textbox(label="Sorted Array")

    # Define what happens when the button is clicked
    sort_button.click(
        fn=sort_array,
        inputs=[array_input, algorithm_choice],
        outputs=result
    )

# Launch the Gradio demo with sharing enabled
demo.launch(share=True)