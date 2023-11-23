import matplotlib.pyplot as plt
import numpy as np

def plot_chromosome(ax, chromosome_length, gene_positions, gene_labels, gene_starts, gene_ends, chromosome_label):
    # Plot chromosome
    ax.plot([0, chromosome_length], [0, 0], color='pink', linewidth=200, zorder=1)

    # Plot gene positions with start and end values
    for start, end, label in zip(gene_starts, gene_ends, gene_labels):
        ax.fill_betweenx(y=[-0.5, 0.5], x1=start, x2=end, color=np.random.rand(3,), label=label, zorder=100)

    # Connect gene labels with arrows and rotate by 90 degrees
    for start, label in zip(gene_starts, gene_labels):
        ax.annotate(label, xy=(start, 0), xytext=(start, -1),
                    arrowprops=dict(arrowstyle='->', color='black'),
                    rotation=90, ha='center', va='center', zorder=100)  # Rotate the text by 90 degrees

    ax.set_yticks([])
    ax.set_xlim(0, chromosome_length)
    ax.set_title(chromosome_label)  # Add chromosome label

# Example data for three chromosomes
chromosome_lengths = [2500000, 3000000, 1500000, 3500000]

# Gene data for each chromosome
gene_positions_chr1 = [0, 1, 2, 3]
gene_labels_chr1 = ['GeneA', 'GeneB', 'GeneC', 'GeneD']
gene_starts_chr1 = [100000, 200000, 300000, 500000]
gene_ends_chr1 = [110000, 220000, 310000, 510000]

gene_positions_chr2 = [0, 1, 2, 3]
gene_labels_chr2 = ['GeneE', 'GeneF', 'GeneG', 'GeneH']
gene_starts_chr2 = [200000, 300000, 400000, 600000]
gene_ends_chr2 = [210000, 320000, 410000, 610000]

gene_positions_chr3 = [0, 1, 2, 3]
gene_labels_chr3 = ['GeneI', 'GeneJ', 'GeneK', 'GeneL']
gene_starts_chr3 = [500000, 600000, 700000, 900000]
gene_ends_chr3 = [510000, 620000, 710000, 910000]

gene_positions_chr4 = [0, 1, 2, 3]
gene_labels_chr4 = ['GeneM', 'GeneN', 'GeneO', 'GeneP']
gene_starts_chr4 = [500000, 600000, 700000, 900000]
gene_ends_chr4 = [510000, 620000, 710000, 910000]
# Create subplots for each chromosome
fig, axs = plt.subplots(1, 4, figsize=(15, 5))  # Adjust the figsize as needed


# Plot each chromosome separately
plot_chromosome(axs[0], chromosome_lengths[0], gene_positions_chr1, gene_labels_chr1, gene_starts_chr1, gene_ends_chr1, 'Chromosome 1')
plot_chromosome(axs[1], chromosome_lengths[1], gene_positions_chr2, gene_labels_chr2, gene_starts_chr2, gene_ends_chr2, 'Chromosome 2')
plot_chromosome(axs[2], chromosome_lengths[2], gene_positions_chr3, gene_labels_chr3, gene_starts_chr3, gene_ends_chr3, 'Chromosome 3')
plot_chromosome(axs[3], chromosome_lengths[3], gene_positions_chr4, gene_labels_chr4, gene_starts_chr4, gene_ends_chr4, 'Chromosome 4')

# Set a common title for all subplots
fig.suptitle('Schematic chromosomes with gene positions')

plt.show()





