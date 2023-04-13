import slideflow as sf
rootpath = '/mnt/pdac/'
P = sf.load_project(rootpath)
dataset=P.dataset(tile_px=299, tile_um='10x')
dataset.summary()


