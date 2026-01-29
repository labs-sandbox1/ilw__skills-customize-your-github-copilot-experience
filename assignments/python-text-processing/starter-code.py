"""
Python Text Processing Assignment
Starter code for text analysis and transformation tasks
"""

# Task 1: Word Frequency Counter
def count_word_frequency(filename):
    """
    Reads a text file and returns a dictionary of word frequencies.
    
    Args:
        filename (str): Path to the text file to analyze
        
    Returns:
        dict: Dictionary with words as keys and their counts as values
    """
    word_count = {}
    
    # TODO: Open and read the file
    # TODO: Process each line, split into words
    # TODO: Clean each word (lowercase, remove punctuation)
    # TODO: Count word frequencies
    
    return word_count


def display_top_words(word_count, n=10):
    """
    Displays the top N most frequent words.
    
    Args:
        word_count (dict): Dictionary of word frequencies
        n (int): Number of top words to display
    """
    # TODO: Sort words by frequency
    # TODO: Display the top N words with their counts
    pass


# Task 2: Text File Transformer
def transform_text(input_file, output_file, transformation):
    """
    Applies a transformation to text and writes to a new file.
    
    Args:
        input_file (str): Path to input text file
        output_file (str): Path to output text file
        transformation (str): Type of transformation to apply
    """
    try:
        # TODO: Read the input file
        # TODO: Apply the selected transformation
        # TODO: Write to the output file
        # TODO: Display confirmation message
        pass
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """Main function to run the text processing program."""
    print("=== Python Text Processing ===\n")
    
    # Example usage for Task 1
    print("Task 1: Word Frequency Counter")
    # TODO: Call count_word_frequency with 'sample.txt'
    # TODO: Display results
    
    print("\nTask 2: Text File Transformer")
    # TODO: Display menu of transformations
    # TODO: Get user input
    # TODO: Call transform_text with user's choice


if __name__ == "__main__":
    main()
