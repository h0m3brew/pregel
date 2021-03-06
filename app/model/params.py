from app.utils.constant import GCN, SYMMETRIC, GCN_POLY
from app.utils.util import get_class_variables
from abc import ABC, abstractmethod


class Params(ABC):
    '''
    Base Class for handling params
    '''

    def __init__(self):
        pass

    def get_variables(self):
        return get_class_variables(self)

class ModelParams(Params):
    '''
    Class for the params used by the underlying models
    '''

    def __init__(self, flags):
        self.model_name = flags.model_name
        self.learning_rate = flags.learning_rate
        self.epochs = flags.epochs
        self.hidden_layer1_size = flags.hidden_layer1_size
        try:
            self.hidden_layer2_size = flags.hidden_layer2_size
        except AttributeError:
            self.hidden_layer2_size = None
        self.dropout = flags.dropout
        self.l2_weight = flags.l2_weight
        self.early_stopping = flags.early_stopping
        self.sparse_features = flags.sparse_features
        try:
            self.support_size = flags.poly_degree + 1
        except AttributeError:
            self.support_size = 1
        self.norm_mode = SYMMETRIC
        self.tensorboard_logs_dir = flags.tensorboard_logs_dir
        if(self.tensorboard_logs_dir == ""):
            self.tensorboard_logs_dir = None
        self.num_exp = flags.num_exp
        self.populate_params()

    def populate_params(self):
        '''
        Method to populate all the params for the model
        '''

        if (self.model_name != GCN_POLY):
            self.support_size = 1


class SparseModelParams(Params):
    '''
    Class for the params that are used when sparse data representation is used.
    '''

    def __init__(self, num_elements, feature_size):
        self.num_elements = num_elements
        self.feature_size = feature_size

class AutoEncoderModelParams(Params):
    '''
    Class for the params that are used by the AutoEncoder models - gcn_ae and gcn_vae.
    '''

    def __init__(self, positive_sample_weight, node_count=-1):
        self.positive_sample_weight = positive_sample_weight
        self.node_count = node_count