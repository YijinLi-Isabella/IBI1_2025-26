# Print the initial dictionary
gene_expression = {'TP53': 12.4, 'EGFR': 15.1, 'BRCA1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}
print("The initial dictionary:")
print(gene_expression)
# Add MYC
gene_expression['MYC'] = 11.6
print("The dictionary with MYC expression:")
print(gene_expression)
# Produce the bar chart
import matplotlib.pyplot as plt
genes = list(gene_expression.keys())
expression_values = list(gene_expression.values())
plt.figure(figsize=(8, 5))  # Set the size of the figure
plt.bar(genes, expression_values, color = 'skyblue')
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels in a Biological Sample")
plt.show()
# The expression level of a specific gene
gene_of_interest = 'TP53'
if gene_of_interest in gene_expression:
    #If the gene is present in the dataset, print its expression level
    print("The expression level of", gene_of_interest, "is", gene_expression[gene_of_interest])
else:
    #If the gene is not present in the dataset, print the error message
    print("Error: the gene", gene_of_interest, "is not present in the dataset.")
# Calculate the average gene expression level
average_expression = sum(expression_values) / len(expression_values)
print(f"The average expression level is {average_expression: .2f}")