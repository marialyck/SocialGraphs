import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
from collections import Counter 

def GetCollarboratingArtists(parent_artist_name,K):
    CLIENT_ID = "4688af49fa6d44888e1e9efc433c05c8"
    CLIENT_SECRET = "88271e39c3504fd99f599872c748ea73"

    credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)
    
    res = spotify.search(parent_artist_name, limit=10, offset=0, type='artist', market=None)
    art_id = res['artists']['items'][0]['id']
    
    albums_pt1 = spotify.artist_albums(art_id, album_type=None, country='US', limit=50)
    
    unique_albums = []
    unique_album_uris = []
    for idx in range(len(albums_pt1['items'])):
        album_name = albums_pt1['items'][idx]['name']        
        album_uri = albums_pt1['items'][idx]['uri']
        if album_name not in unique_albums:
            unique_albums.append(album_name)
            unique_album_uris.append(album_uri)
    
    nodes_list = [] #artist is featured by another artist
    collab_list = [] #edges
    unique_songs = []
    collab_count_dic = {}
    
    for idx in range(len(unique_album_uris)):
        album_tracks = spotify.album_tracks(unique_album_uris[idx],limit=None,offset=0)
        for j in range(len(album_tracks['items'])):
            artists = album_tracks['items'][j]['artists'][0]['name']
            name = album_tracks['items'][j]['name']
#            if parent_artist_name in name and parent_artist_name != artists and name not in unique_songs:
#                unique_songs.append(name)
#                guest_list.append((artists,parent_artist_name))
            if len(album_tracks['items'][j]['artists']) > 1:
                new_artists = []
                for i in range(len(album_tracks['items'][j]['artists'])):
                    new_artists.append(album_tracks['items'][j]['artists'][i]['name'])
                if parent_artist_name in new_artists and name not in unique_songs:
                    unique_songs.append(name)
                    host = album_tracks['items'][j]['artists'][0]['name']
                    if host != parent_artist_name:
                        if host in collab_count_dic:
                            collab_count_dic[host] += 1
                        else:
                            collab_count_dic[host] = 1
                        guest = parent_artist_name
                        nodes_list.append(host)
                        collab_list.append((host,guest))
                    else:
                        for k in range(1,len(album_tracks['items'][j]['artists'])):
                            guest = album_tracks['items'][j]['artists'][k]['name']
                            if guest in collab_count_dic:
                                collab_count_dic[guest] += 1
                            else:
                                collab_count_dic[guest] = 1
                            nodes_list.append(guest)
                            collab_list.append((host,guest))
 
    k = Counter(collab_count_dic) 
    high = k.most_common(K) #three most collaborating artists
    high_new = []
    print('Most frequent collaboration partners for: ', parent_artist_name)
    for i in high:
        high_new.append(i[0])
        print(i[0]," :",i[1]," ") 
    print('\n')
    return high_new,nodes_list,collab_list