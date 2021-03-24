from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))


# Use positional argument unpacking to create the same behavior as the join function.
def myjoin(*args):
  string = args[0]
  for argument in args[1:]:
    string += "/" + argument
  return string

print(myjoin(path_segment_1, path_segment_2, path_segment_3))