def set_seed(dls, x=42): # added this line from @marii-moe's comment
    random.seed(x)
    dls.rng.seed(x) # added this line from @marii-moe's comment
    np.random.seed(x)
    torch.manual_seed(x)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    if torch.cuda.is_available(): torch.cuda.manual_seed_all(x)
