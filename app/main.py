import re

# Internal imports
from app.models import AnalysisModel, SynthesisModel
from app.views import AnalysisView, SynthesisView
from app.controllers import AnalysisController, SynthesisController
from app.data import OpcodeData


def run():
    print('Welcome, let\'s assemble some assembly!\n')
    path = 'assembler/asm-2.txt'

    # Run analysis on the assembly file and return the synthesis_model
    synthesis_model = AnalysisController(
        model=AnalysisModel(
            assembly_file_path=path,
            pattern=r'(\s*([_a-z]\w*)\s*:)?\s*([A-Z]*\s*[A-Z]\s*,{0,1}\s*[A-Z]{0,1})\s*(#([0-9a-fA-F]{0,2})\s*)?(\s*('
                    r'[_a-z]\w*)\s*)?',
            label_definition_group=2,
            label_call_group=7,
            byte_definition_group=5
        ),
        view=AnalysisView
    ).run()

    # Set the opcode table in the synthesis model
    synthesis_model.opcode_table = OpcodeData.get_opcode_data()

    # Run the synthesis to generate machine code
    SynthesisController(model=synthesis_model, view=SynthesisView).run()
