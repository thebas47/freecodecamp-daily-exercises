# Listas para controle de unidades de video e do drive
v_units = ['B', 'KB', 'MB', 'GB']
d_units = ['GB', 'TB']

# Dicionário responsável por definir a padronização das medidas gerais para bytes
byte_norms = {'B': 1, 'KB': 1000, 'MB': 1000**2, 'GB': 1000**3, 'TB': 1000**4}

def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    
    # Verifica unidade de video
    if video_unit not in v_units:
        return 'Invalid video unit'

    # Verifica unidade do drive
    if drive_unit not in d_units:
        return 'Invalid drive unit'

    # Padronizando o tamanho de video e do drive em bytes
    drive_bytes = drive_size * byte_norms[drive_unit]
    video_bytes = video_size * byte_norms[video_unit]

    # Calcula quantos vídeos o drive suporta
    calc = drive_bytes // video_bytes

    return calc

print(number_of_videos(500, "MB", 100, "GB"))
print(number_of_videos(1, "TB", 10, "TB"))
print(number_of_videos(2000, "MB", 100000, "MB"))
print(number_of_videos(500000, "KB", 2, "TB"))
print(number_of_videos(1.5, "GB", 2.2, "TB"))
