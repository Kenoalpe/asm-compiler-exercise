# Internal imports
from app.models import AnalysisModel
from app.views import AnalysisView, SynthesisView
from app.controllers import AnalysisController, SynthesisController
from app.util import FileUtils
from app.data import OpcodeData


def run():
    print('Welcome, let\'s assemble some assembly!\n')
    path = 'assembler/asm-4.txt'

    # Run analysis on the assembly file and return the synthesis_model
    synthesis_model = AnalysisController(
        model=AnalysisModel(
            assembly_file_path=path,
            pattern=r'(\s*([_a-z]\w*)\s*:)?\s*([A-Z]*\s*[A-Z]\s*,{0,1}[A-Z]{0,1})\s*(#{0,1}([0-9A-F]{,2})\s*)?(\s*([_a-z]\w*)\s*)?',
            label_definition_group=2,
            label_call_group=7,
            byte_definition_group=4
        ),
        view=AnalysisView
    ).run()

    # Set the opcode table in the synthesis model
    synthesis_model.opcode_table = OpcodeData.get_opcode_data()

    # Run the synthesis to generate machine code
    # ToDo change parse to view
    FileUtils.parse_array_to_file('assembler/opcode.txt', SynthesisController(
        model=synthesis_model, view=SynthesisView).run())
