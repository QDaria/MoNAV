#!/usr/bin/env python
# coding: utf-8

# # DataSynthesizer (random mode)

# DataSynthesizer generates synthetic data that simulates a given dataset.
# 
# It aims to facilitate the collaborations between data scientists and owners of sensitive data. It applies Differential Privacy techniques to achieve strong privacy guarantee.
# #https://github.com/DataResponsibly/DataSynthesizer/blob/master/docs/cr-datasynthesizer-privacy.pdf

# ## Step 1 import packages

# In[1]:


from DataSynthesizer.DataDescriber import DataDescriber
from DataSynthesizer.DataGenerator import DataGenerator
from DataSynthesizer.ModelInspector import ModelInspector
from DataSynthesizer.lib.utils import read_json_file, display_bayesian_network

import pandas as pd


# In[54]:


# help(DataDescriber)
#print(dir(DataDescriber))
print(id(DataDescriber))


# In[56]:


# hasattr(obj, name)
# obj is the object under inspection.
# name is the name (as a string) of the possible attribute.
hasattr(DataDescriber, "type(int)")


# In[ ]:





# ## Step 2 user-defined parameteres

# In[25]:


# input dataset
#input_data = './data/adult_ssn.csv'
input_data = '/Users/m0/Documents/GitHub/MoHoushmand.github.io/DATA/data/adult_ssn.csv'
# location of two output files
mode = 'random_mode'
#description_file =  f'.DATA/out/{mode}/description.json'
description_file = f'/Users/m0/Documents/GitHub/MoHoushmand.github.io/DATA/out/{mode}/description.json'
#synthetic_data = f'.DATA/out/{mode}/sythetic_data.csv'
synthetic_data = f'/Users/m0/Documents/GitHub/MoHoushmand.github.io/DATA/out/{mode}/sythetic_data.csv'


# In[26]:


# An attribute is categorical if its domain size is less than this threshold.
# Here modify the threshold to adapt to the domain size of "education" (which is 14 in input dataset).
threshold_value = 20 

# Number of tuples generated in synthetic dataset.
num_tuples_to_generate = 32561 # Here 32561 is the same as input dataset, but it can be set to another number.


# ## Step 3 DataDescriber
# 1. Instantiate a DataDescriber.
# 2. Compute the statistics of the dataset.
# 3. Save dataset description to a file on local machine.

# In[27]:


describer = DataDescriber(category_threshold=threshold_value)
describer.describe_dataset_in_random_mode(input_data)
describer.save_dataset_description_to_file(description_file)


# ## Step 4 generate synthetic dataset
# 1. Instantiate a DataGenerator.
# 2. Generate a synthetic dataset.
# 3. Save it to local machine.

# In[28]:


generator = DataGenerator()
generator.generate_dataset_in_random_mode(num_tuples_to_generate, description_file)
generator.save_synthetic_data(synthetic_data)


# ## Step 5 compare the statistics of input and sythetic data (optional)
# The synthetic data is already saved in a file by step 4. The ModelInspector is for a quick test on the similarity between input and synthetic datasets.
# 
# ### 5.1 instantiate a ModelInspector.
# It needs input dataset, synthetic dataset, and attribute description.

# In[29]:


# Read both datasets using Pandas.
input_df = pd.read_csv(input_data, skipinitialspace=True)
synthetic_df = pd.read_csv(synthetic_data)
# Read attribute description from the dataset description file.
attribute_description = read_json_file(description_file)['attribute_description']

inspector = ModelInspector(input_df, synthetic_df, attribute_description)


# ### 5.2 compare histograms between input and synthetic datasets.

# In[30]:


for attribute in synthetic_df.columns:
    inspector.compare_histograms(attribute)


# In[31]:


inspector.mutual_information_heatmap()


# # DataSynthesizer Usage (independent attribute mode)
# 
# ## Step 1 import packages

# ## Step 2 user-defined parameteres

# In[32]:


# location of two output files
mode = 'independent_attribute_mode'
description_file = f'/Users/m0/Documents/GitHub/MoHoushmand.github.io/DATA/out/{mode}/description.json'
synthetic_data = f'/Users/m0/Documents/GitHub/MoHoushmand.github.io/DATA/out/{mode}/sythetic_data.csv'


# In[33]:


# An attribute is categorical if its domain size is less than this threshold.
# Here modify the threshold to adapt to the domain size of "education" (which is 14 in input dataset).
threshold_value = 20 

# specify categorical attributes
categorical_attributes = {'education': True}

# specify which attributes are candidate keys of input dataset.
candidate_keys = {'age': False}

# Number of tuples generated in synthetic dataset.
num_tuples_to_generate = 32561 # Here 32561 is the same as input dataset, but it can be set to another number.


# 

# ## Step 3 DataDescriber
# 1. Instantiate a DataDescriber.
# 2. Compute the statistics of the dataset.
# 3. Save dataset description to a file on local machine.

# In[35]:


describer = DataDescriber(category_threshold=threshold_value)
describer.describe_dataset_in_independent_attribute_mode(dataset_file=input_data,
                                                         attribute_to_is_categorical=categorical_attributes,
                                                         attribute_to_is_candidate_key=candidate_keys)
describer.save_dataset_description_to_file(description_file)


# ## Step 4 generate synthetic dataset
# 1. Instantiate a DataGenerator.
# 2. Generate a synthetic dataset.
# 3. Save it to local machine.

# In[37]:


generator = DataGenerator()
generator.generate_dataset_in_independent_mode(num_tuples_to_generate, description_file)
generator.save_synthetic_data(synthetic_data)


# ## Step 5 compare the statistics of input and sythetic data (optional)
# The synthetic data is already saved in a file by step 4. The ModelInspector is for a quick test on the similarity between input and synthetic datasets.
# 
# 
# ## 5.1 instantiate a ModelInspector.
# It needs input dataset, synthetic dataset, and attribute description.

# In[38]:


# Read both datasets using Pandas.
input_df = pd.read_csv(input_data, skipinitialspace=True)
synthetic_df = pd.read_csv(synthetic_data)
# Read attribute description from the dataset description file.
attribute_description = read_json_file(description_file)['attribute_description']

inspector = ModelInspector(input_df, synthetic_df, attribute_description)


# ## 5.2 compare histograms between input and synthetic datasets.

# In[40]:


for attribute in synthetic_df.columns:
    inspector.compare_histograms(attribute)


# ## 5.3 compare pairwise mutual information

# In[41]:


inspector.mutual_information_heatmap()


# # DataSynthesizer Usage (correlated attribute mode)

# ## Step 1 import packages

# ## Step 2 user-defined parameteres

# In[42]:


# location of two output files
mode = 'correlated_attribute_mode'
description_file = f'/Users/m0/Documents/GitHub/MoHoushmand.github.io/DATA/out/{mode}/description.json'
synthetic_data = f'/Users/m0/Documents/GitHub/MoHoushmand.github.io/DATA/out/{mode}/sythetic_data.csv'


# In[43]:


# An attribute is categorical if its domain size is less than this threshold.
# Here modify the threshold to adapt to the domain size of "education" (which is 14 in input dataset).
threshold_value = 20

# specify categorical attributes
categorical_attributes = {'education': True}

# specify which attributes are candidate keys of input dataset.
candidate_keys = {'ssn': True}

# A parameter in Differential Privacy. It roughly means that removing a row in the input dataset will not 
# change the probability of getting the same output more than a multiplicative difference of exp(epsilon).
# Increase epsilon value to reduce the injected noises. Set epsilon=0 to turn off differential privacy.
epsilon = 1

# The maximum number of parents in Bayesian network, i.e., the maximum number of incoming edges.
degree_of_bayesian_network = 2

# Number of tuples generated in synthetic dataset.
num_tuples_to_generate = 1000 # Here 32561 is the same as input dataset, but it can be set to another number.


# ## Step 3 DataDescriber
# Instantiate a DataDescriber.
# Compute the statistics of the dataset.
# Save dataset description to a file on local machine.

# In[44]:


describer = DataDescriber(category_threshold=threshold_value)
describer.describe_dataset_in_correlated_attribute_mode(dataset_file=input_data, 
                                                        epsilon=epsilon, 
                                                        k=degree_of_bayesian_network,
                                                        attribute_to_is_categorical=categorical_attributes,
                                                        attribute_to_is_candidate_key=candidate_keys)
describer.save_dataset_description_to_file(description_file)


# ## Step 4 generate synthetic dataset
# 1. Instantiate a DataGenerator.
# 2. Generate a synthetic dataset.
# 3. Save it to local machine.

# In[45]:


generator = DataGenerator()
generator.generate_dataset_in_correlated_attribute_mode(num_tuples_to_generate, description_file)
generator.save_synthetic_data(synthetic_data)


# ## Step 5 compare the statistics of input and sythetic data (optional)
# The synthetic data is already saved in a file by step 4. The ModelInspector is for a quick test on the similarity between input and synthetic datasets.
# 
# ## 5.1 instantiate a ModelInspector.
# It needs input dataset, synthetic dataset, and attribute description

# In[47]:


# Read both datasets using Pandas.
input_df = pd.read_csv(input_data, skipinitialspace=True)
synthetic_df = pd.read_csv(synthetic_data)
# Read attribute description from the dataset description file.
attribute_description = read_json_file(description_file)['attribute_description']

inspector = ModelInspector(input_df, synthetic_df, attribute_description)


# ## 5.2 compare histograms between input and synthetic datasets.

# In[48]:


for attribute in synthetic_df.columns:
    inspector.compare_histograms(attribute)


# ## 5.3 compare pairwise mutual information

# In[50]:


inspector.mutual_information_heatmap()


# In[1]:


i = rand(1..10)
unless i % 2 == 0
    puts "#{i} is odd"
else
    puts "#{i} is even"
end


# In[ ]:




