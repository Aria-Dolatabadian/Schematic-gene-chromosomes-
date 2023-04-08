import matplotlib.pyplot as plt

# Define the chromosome lengths
chrom_lengths = [100, 90, 80, 70, 60, 50, 40, 30, 20, 100]

# Define the gene names and their positions on each chromosome
gene_names = [['Gene A', 'Gene B', 'Gene C', 'Gene D', 'Gene E'],
              ['Gene F', 'Gene G', 'Gene H', 'Gene I'],
              ['Gene J', 'Gene K', 'Gene L'],
              ['Gene M', 'Gene N', 'Gene O'],
              ['Gene P', 'Gene Q', 'Gene R'],
              ['Gene S', 'Gene T'],
              ['Gene U', 'Gene V'],
              ['Gene W'],
              ['Gene X'],
              ['Gene Y', 'Gene Z']]

gene_positions = [[10, 30, 50, 75, 90],
                  [10, 30, 50, 70],
                  [10, 30, 50],
                  [10, 30, 50],
                  [10, 30, 50],
                  [10, 30],
                  [10, 30],
                  [10],
                  [5],
                  [30,60]]

# Define the figure and axis
fig, axs = plt.subplots(nrows=len(chrom_lengths), figsize=(8, 10))

# Loop through the chromosomes and plot each one
for i in range(len(chrom_lengths)):
    chrom_length = chrom_lengths[i]
    positions = gene_positions[i]
    names = gene_names[i]

    # Plot the chromosome as a line
    axs[i].plot([0, chrom_length], [0, 0], linewidth=3, color='black')

    # Plot the genes as squares
    gene_height = 0.5
    gene_width = 5
    for name, position in zip(names, positions):
        axs[i].add_patch(plt.Rectangle((position - gene_width/2, -gene_height/2), gene_width, gene_height, color='pink'))
        axs[i].text(position, gene_height, name, ha='center', va='bottom')

    # Set the x and y limits and labels
    axs[i].set_xlim([0, chrom_length])
    axs[i].set_ylim([-gene_height, gene_height*2])
    axs[i].set_xlabel('Chr {}'.format(i+1), loc='left')
    axs[i].set_yticks([])

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()
