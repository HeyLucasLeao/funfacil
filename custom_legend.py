def custom_legend(fig, nameSwap):
    for i, dat in enumerate(fig.data):
        for elem in dat:
            if elem == 'name':
                fig.data[i].name = nameSwap[fig.data[i].name]
    return(fig)

#custom_legend(fig=fig,nameSwap = {'0': 'Sim', '1': 'Não'})
