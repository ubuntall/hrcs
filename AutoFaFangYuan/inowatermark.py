from nowatermark import WatermarkRemover

path = './imgs/'

watermark_template_filename = path + 'mask.png'
remover = WatermarkRemover()
remover.load_watermark_template(watermark_template_filename)

remover.remove_watermark(path + '99.jpg', path + '99-result.jpg')
# remover.remove_watermark(path + 'anjuke4.jpg', path + 'anjuke4-result.jpg')